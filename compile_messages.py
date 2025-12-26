#!/usr/bin/env python
"""
Compile .po files to .mo files without requiring gettext tools.
Proper implementation with correct MO file format.
"""
import os
import struct


def unescape(s):
    """Unescape special characters in PO strings"""
    s = s.replace('\\n', '\n')
    s = s.replace('\\t', '\t')
    s = s.replace('\\r', '\r')
    s = s.replace('\\"', '"')
    s = s.replace('\\\\', '\\')
    return s


def parse_po_file(po_file):
    """Parse a .po file and return a dictionary of msgid -> msgstr"""
    messages = {}
    
    with open(po_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_msgid = []
    current_msgstr = []
    in_msgid = False
    in_msgstr = False
    
    for line in lines:
        line = line.rstrip('\n\r')
        
        if line.startswith('msgid "'):
            # Save previous message
            if current_msgid and current_msgstr:
                msgid = unescape(''.join(current_msgid))
                msgstr = unescape(''.join(current_msgstr))
                if msgid:  # Don't save empty msgid (header)
                    messages[msgid] = msgstr
            
            in_msgid = True
            in_msgstr = False
            current_msgid = [line[7:-1]]  # Remove 'msgid "' and trailing '"'
            current_msgstr = []
            
        elif line.startswith('msgstr "'):
            in_msgstr = True
            in_msgid = False
            current_msgstr = [line[8:-1]]  # Remove 'msgstr "' and trailing '"'
            
        elif line.startswith('"') and line.endswith('"'):
            # Continuation line
            text = line[1:-1]
            if in_msgid:
                current_msgid.append(text)
            elif in_msgstr:
                current_msgstr.append(text)
                
        elif line == '' or line.startswith('#'):
            # Empty line or comment
            pass
    
    # Don't forget the last message
    if current_msgid and current_msgstr:
        msgid = unescape(''.join(current_msgid))
        msgstr = unescape(''.join(current_msgstr))
        if msgid:
            messages[msgid] = msgstr
    
    return messages


def write_mo_file(messages, mo_file):
    """Write messages to a .mo file"""
    # Sort keys for binary search
    keys = sorted(messages.keys())
    
    # Prepare the strings
    offsets = []
    ids = b''
    strs = b''
    
    for key in keys:
        # Encode to UTF-8
        key_bytes = key.encode('utf-8')
        value_bytes = messages[key].encode('utf-8')
        
        offsets.append((len(ids), len(key_bytes), len(strs), len(value_bytes)))
        ids += key_bytes + b'\x00'
        strs += value_bytes + b'\x00'
    
    # Calculate offsets
    # Header: 7 * 4 = 28 bytes
    # Original strings table: len(keys) * 8 bytes
    # Translation strings table: len(keys) * 8 bytes
    keystart = 28 + len(keys) * 8 * 2
    valuestart = keystart + len(ids)
    
    # Build offset tables
    koffsets = b''
    voffsets = b''
    
    for o1, l1, o2, l2 in offsets:
        koffsets += struct.pack('<II', l1, o1 + keystart)
        voffsets += struct.pack('<II', l2, o2 + valuestart)
    
    # MO file header (little-endian)
    header = struct.pack(
        '<IIIIIII',
        0x950412de,      # Magic number
        0,               # Version
        len(keys),       # Number of strings
        28,              # Offset of original strings table
        28 + len(keys) * 8,  # Offset of translation strings table
        0,               # Size of hashing table
        0                # Offset of hashing table
    )
    
    with open(mo_file, 'wb') as f:
        f.write(header)
        f.write(koffsets)
        f.write(voffsets)
        f.write(ids)
        f.write(strs)
    
    return len(keys)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base_dir, 'locale')
    
    languages = ['tr', 'sq']
    
    for lang in languages:
        po_file = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
        mo_file = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
        
        if os.path.exists(po_file):
            try:
                messages = parse_po_file(po_file)
                count = write_mo_file(messages, mo_file)
                print(f"OK Compiled {lang}/LC_MESSAGES/django.po -> django.mo ({count} messages)")
            except Exception as e:
                print(f"ERROR compiling {lang}: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"NOT FOUND: {po_file}")


if __name__ == '__main__':
    main()
