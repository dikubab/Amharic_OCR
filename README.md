
## Detection and Recognition of Amharic Scene Text using the toolbox  

This toolbox is an open-source toolbox based and for details of installation and related information see (https://github.com/open-mmlab/mmocr. 

Generally, Geʽez/Abugida/Ethiopic script has up to 519 characters. For Amharic, we use 289-319 characters depending on whether we use Ethiopic numerals and punctuation. 

 
## Amharic Text Detection dataset preprocessing

We have two datasets for the detection task. HUST-ART is the real word dataset, and HUST-AST is the synthetic dataset. HUST-ART consists of 1500 training images and 700 test images. HUST-AST comprises 75,904 training images.
 To convert the dataset labels to MMOCR format, use tools/data/textdet/icdar_converter.py as follows

 python tools/data/textdet/icdar_converter.py det_datasets/HUST-ART -o det_datasets/HUST-ART -d icdar2015 --split-list training test

## Amharic Text Recognition  
We have two training sets and two test sets datasets. Tana (TN) and Waliya (WL) training sets consist of 2.85 and 6M cropped words, respectively. HUST-ART and ABE test sets consist of 4039 and 5218 text images. We also have a validation dataset composed of 14835 text images, which is the training part of HUST-ART and ABE. All five datasets are in LMDB format.  

The toolbox usage
1.  In the directory configs/_base_/recog_pipelines/, you have different pipelines you must change dict(type='LoadImageFromFile') to dict(type='LoadImageFromLMDB'),   
2.  In the directory configs/_base_/recog_datasets/, you need to modify the path of test and train datasets.
3.  In the directory mmocr/models/textrecog/convertors/ base.py define the dictionary using the 314 Amharic characters. No need to worry we have modified it. Based on your character set, modify dict_type in all other related files. We have modified the configs/textrecog/satrn/satrn_small.py settings. You can use it as an example.  
The datasets for both detection and recognition can be downloaded from the website https://github.com/dikubab/HUST-ASTD/blob/main/index.md. 

The Waliya-related LMDB dataset link will be provided very soon.
1.  Test and Validation sets LMDB https://mega.nz/folder/Ub0SnBBa#Fh6pFqbvXVxsa7OJPfJEwA
2.  Tana(TN) LMDB https://mega.nz/folder/NGcC1DaQ#soagog8p_LgOnm6Gx9wdCQ
## Citation

If you find our datasets useful in your research, please consider cite:

```bibtex

@article{dikubab2022comprehensive,
  title={Comprehensive benchmark datasets for Amharic scene text detection and recognition},
  author={Dikubab, Wondimu and Liang, Dingkang and Liao, Minghui and Bai, Xiang},
  journal={Science China Information Sciences, Vol. 65, Special Focus on Deep Learning for Computer Vision, Article number: 160106},
  year={2022}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).


