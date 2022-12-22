from molsysmt._private.digestion import digest

@digest(form='file:mmtf')
def to_string_aminoacids1(item, group_indices='all', digest=True):

    from . import to_mmtf_MMTFDecoder
    from ..mmtf_MMTFDecoder import to_string_aminoacids1 as mmtf_MMTFDecoder_to_string_aminoacids1

    tmp_item = to_mmtf_MMTFDecoder(item, digest=False)
    tmp_item = mmtf_MMTFDecoder_to_string_aminoacids1(tmp_item, group_indices=group_indices, digest=False)

    return tmp_item

