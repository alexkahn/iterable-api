class Mapper:
    def __init__(self, initial=None):
        self._mapping = {}
        if initial:
            self._mapping.update(initial)

    def _add(self, source, dest):
        self._mapping[source] = dest

    def remap_key(self, source, dest):
        self._add(source, dest)

    def remap(self, data):
        return self._exec(data)

    def _exec(self, src_dict):
        dest = dict()

        if not src_dict:
            raise AttributeError('The source dictionary cannot be  empty or None')

        for key, value in src_dict.items():
            try:
                new_key = self._mapping[key]
                dest[new_key] = value
            except KeyError:
                dest[key] = value
        return dest
