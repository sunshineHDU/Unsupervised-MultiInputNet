Lili Lin, Qiujian Li, Bin Gao, Yuxiang Yan, [**Wenhui Zhou**](https://faculty.hdu.edu.cn/jsjxy/zwh_en/main.htm), and Ercan Engin Kuruoglu, Unsupervised Learning of Light Field Depth Estimation with Spatial and Angular Consistencies. Neurocomputing, 2022. 501: p. 113--122.  https://doi.org/10.1016/j.neucom.2022.06.011   

![image](https://github.com/windyz77/Unsupervised-Light-Field-Depth-Estimation/blob/master/net.png)


train Requirements
====================================
    pip install -r requirements.txt

dataset
====================================
We used the HCI 4D LF benchmark for training and evaluation. Please refer to the [benchmark website](https://lightfield-analysis.uni-konstanz.de/) for details.

train 
====================================
    python multidepth_main.py

    --model_name MultiDepth 

    --data_path /your/path/to/full_data

    --total_epoch 500

    --batch_size 2

    --train_txt_path /your/path/train_val_txt/4dlf_7x7star_train.txt

    --output_path=./output/check_code_oldcode

test
====================================
    change train_mode = False

    python multidepth_main.py

    --model_name MultiDepth 

    --data_path /your/path/to/full_data

    --val_txt_path' /your/path/train_val_txt/4dlf_7x7star_val.txt

    --checkpoint_path ./output/check_code1/MultiDepth/your model
