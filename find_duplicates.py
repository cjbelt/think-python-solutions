import os

def list_file_suffix(path, suffix):
    t = []

    for name in os.listdir(path):
        new_path = os.path.join(path, name)

        if name.endswith(suffix):
            t.append(new_path)
        elif os.path.isdir(new_path):
            t = t + list_file_suffix(new_path, suffix)

    return t

def make_checksums(t):
    checksums = {}

    for path in t:
        cmd = 'md5sum ' + path
        fp = os.popen(cmd)
        res = fp.read()
        file_code = res.split(' ')[0]
        checksums.setdefault(file_code, [])
        checksums[file_code].append(path)
        stat = fp.close()

    return checksums

def find_duplicates(path, suffix):
    t = list_file_suffix(path, suffix)
    checksums = make_checksums(t)
    duplicates = []

    for file_code in checksums:
        if len(checksums[file_code]) > 1:
            duplicates.append(checksums[file_code])

    return duplicates

# print(find_duplicates(os.getcwd(), '.py'))
