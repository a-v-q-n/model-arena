#!/usr/bin/env python3
"""
Parse opencode stats --models output and compute token diffs.

Usage:
  python3 scripts/token-diff.py <model-id> < <stats-output>
  python3 scripts/token-diff.py <model-id> <before-file> <after-file>

Output: JSON with {input_tokens, output_tokens, cache_read, cache_write, cost, messages}
"""
import re
import sys
import json


def strip_ansi(text):
    return re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', text)


def parse_model_stats(text, model_id):
    """Parse stats output and return data for the given model_id."""
    text = strip_ansi(text)
    lines = text.split('\n')

    in_target = False
    data = {}

    for line in lines:
        cleaned = line.replace('│', '').strip()

        if not cleaned:
            continue

        if model_id in cleaned and not cleaned.startswith('Messages') and \
           not cleaned.startswith('Input') and not cleaned.startswith('Output') and \
           not cleaned.startswith('Cache') and not cleaned.startswith('Cost'):
            in_target = True
            continue

        if not in_target:
            continue

        # Stop at next separator or end
        if cleaned.startswith('├') or cleaned.startswith('└') or cleaned.startswith('┌'):
            break

        # Parse data lines
        m = re.match(r'Messages\s+(\d+)', cleaned)
        if m:
            data['messages'] = int(m.group(1))
            continue

        m = re.match(r'Input Tokens\s+([\d.]+)([KMB]?)', cleaned)
        if m:
            data['input_tokens'] = _parse_suffixed(m)
            continue

        m = re.match(r'Output Tokens\s+([\d.]+)([KMB]?)', cleaned)
        if m:
            data['output_tokens'] = _parse_suffixed(m)
            continue

        m = re.match(r'Cache Read\s+([\d.]+)([KMB]?)', cleaned)
        if m:
            data['cache_read'] = _parse_suffixed(m)
            continue

        m = re.match(r'Cache Write\s+([\d.]+)([KMB]?)', cleaned)
        if m:
            data['cache_write'] = _parse_suffixed(m)
            continue

        m = re.match(r'Cost\s+\$?([\d.]+)', cleaned)
        if m:
            data['cost'] = float(m.group(1))
            continue

    return data


def _parse_suffixed(m):
    val = float(m.group(1))
    suffix = m.group(2)
    if suffix == 'K':
        val *= 1000
    elif suffix == 'M':
        val *= 1000000
    elif suffix == 'B':
        val *= 1000000000
    return int(round(val))


def zero():
    return {'input_tokens': 0, 'output_tokens': 0, 'cache_read': 0, 'cache_write': 0, 'cost': 0.0, 'messages': 0}


if __name__ == '__main__':
    if len(sys.argv) == 2:
        text = sys.stdin.read()
        data = parse_model_stats(text, sys.argv[1])
        if not data:
            data = zero()
        print(json.dumps(data))
    elif len(sys.argv) == 4:
        with open(sys.argv[2]) as f:
            before = parse_model_stats(f.read(), sys.argv[1])
        with open(sys.argv[3]) as f:
            after = parse_model_stats(f.read(), sys.argv[1])
        b = before if before else zero()
        a = after if after else zero()
        diff = {
            'input_tokens': a['input_tokens'] - b['input_tokens'],
            'output_tokens': a['output_tokens'] - b['output_tokens'],
            'cache_read': a['cache_read'] - b['cache_read'],
            'cache_write': a['cache_write'] - b['cache_write'],
            'cost': round(a['cost'] - b['cost'], 6),
            'messages': a['messages'] - b['messages'],
        }
        print(json.dumps(diff))
    else:
        print('Usage: token-diff.py <model-id> [<before-file> <after-file>]', file=sys.stderr)
        sys.exit(1)
