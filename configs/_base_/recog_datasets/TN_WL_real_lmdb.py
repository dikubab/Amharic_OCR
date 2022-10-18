# Text Recognition Training set, including:
# Synthetic Datasets: SynthText, SynthAdd, Syn90k
# Real Dataset: ABE, HUST-ART, TN, WL

lmdb_root1 = '/home/xwang/vedastr/datasets/train/TN/'
lmdb_root2 = '/home/xwang/vedastr/datasets/train/WL/'
lmdb_root3 = '/home/xwang/vedastr/datasets/valid/valid_lmdb'

train1 = dict(
    type='OCRDataset',
    img_prefix=lmdb_root1 ,
    ann_file=lmdb_root1 ,
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='lmdb',
        parser=dict(
            type='LineJsonParser',
            keys=['filename', 'text'])),
    pipeline=None,
    test_mode=False)
train2 = dict(
    type='OCRDataset',
    img_prefix=lmdb_root2 ,
    ann_file=lmdb_root2 ,
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='lmdb',
        parser=dict(
            type='LineJsonParser',
            keys=['filename', 'text'])),
    pipeline=None,
    test_mode=False)
train3 = dict(
    type='OCRDataset',
    img_prefix=lmdb_root3 ,
    ann_file=lmdb_root3 ,
    loader=dict(
        type='AnnFileLoader',
        repeat=50,
        file_format='lmdb',
        parser=dict(
            type='LineJsonParser',
            keys=['filename', 'text'])),
    pipeline=None,
    test_mode=False)


train_list = [train1, train2, train3]
