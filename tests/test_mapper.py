from lib.iterable.resources.utils import Mapper


def test_mapper_initialization():
    mapper = Mapper({'foo': 'bar', 'bar': 'baz'})
    assert mapper._mapping == {'foo': 'bar', 'bar': 'baz'}


def test_mapper_renames_keys():
    mapper = Mapper()
    mapper.remap_key('source', 'dest')
    remapped = mapper.remap({'source': True})
    assert remapped == {'dest': True}
