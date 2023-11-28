from copy import copy
import subprocess
from glob import glob
import os
import shutil

# パラメータ
CONFIG = {

#-----------------<<<<train>>>>------------------------

    # 全体変数
    "mode": "train",
     # train or pred

    #学習用データ
    "source": "C:/Users/nouga/Desktop/Tamura/datasets/remove_RBC",

    #保存先
    "save_path": "results/glo_result",

    "batch_size" : "4",

    "cn_input": "512",  # generatorへの入力サイズ
    "ld_input": "512", #discriminatorへの入力サイズ

    "init_model_cn": "C:/Users/nouga/Desktop/Tamura/GLCIC/results/glo_result2/phase_3/model_cn_step15000",  # generator事前学習済みモデルのパス
    "init_model_cd": "C:/Users/nouga/Desktop/Tamura/GLCIC/results/glo_result2/phase_3/model_cd_step15000", #discriminator事前学習済みモデルのパス

    "max_holes": "15", #穴あきの個数

    #穴の大きさ
    "hole_min_w": "5",
    "hole_max_w" : "40",
    "hole_min_h" : "5",
    "hole_max_h" : "40",

    "steps_1" : "5000",
    "steps_2" : "800",
    "steps_3" : "15000",
    "snaperiod_1" : "2500",
    "snaperiod_2" : "400",
    "snaperiod_3" : "7500",


#----------<<<<predict>>>>---------

    "cn_model_path" : "C:/Users/nouga/Desktop/Tamura/GLCIC/results/glo_result/phase_3/model_cn_step10000",
    "config_path" : "C:/Users/nouga/Desktop/Tamura/GLCIC/results/glo_result/config.json",
    "input_img" : "C:/Users/nouga/Desktop/Tamura/GLCIC/datasets/512_remove_RBC_img/*.jpg",
    "output_img" : "C:/Users/nouga/Desktop/Tamura/GLCIC/results/output_img",

    "input_labels" : "C:/Users/nouga/Desktop/Tamura/GLCIC/datasets/labels"
    




}

if __name__ == "__main__":
    # 訓練モード
    if CONFIG["mode"] == "train":
        print(CONFIG["mode"])
        subprocess.call('python train.py ' 
                        + CONFIG["source"] + ' ' +
                         CONFIG["save_path"] +  
                         ' --data_parallel ' +
                        ' --bsize ' + CONFIG["batch_size"] +
                        ' --cn_input_size ' + CONFIG["cn_input"] +
                        ' --ld_input_size ' + CONFIG["ld_input"] +
                        ' --init_model_cn ' + CONFIG["init_model_cn"] +
                        ' --init_model_cd ' + CONFIG["init_model_cd"] +
                        ' --max_holes ' + CONFIG["max_holes"] +
                        ' --hole_min_w ' + CONFIG["hole_min_w"] +
                        ' --hole_max_w ' + CONFIG["hole_max_w"] +
                        ' --hole_min_h ' + CONFIG["hole_min_h"] +
                        ' --hole_max_h ' + CONFIG["hole_max_h"] +
                        ' --steps_1 ' + CONFIG["steps_1"] +
                        ' --steps_2 ' + CONFIG["steps_2"] +
                        ' --steps_3 ' + CONFIG["steps_3"] +
                        ' --snaperiod_1 ' + CONFIG["snaperiod_1"] +
                        ' --snaperiod_2 ' + CONFIG["snaperiod_2"] +
                        ' --snaperiod_3 ' + CONFIG["snaperiod_3"] 

                        )

    elif CONFIG["mode"] == "pred":
        print(CONFIG["mode"])
        count = 1

        for file_name in glob(CONFIG["input_img"]):

            basename = os.path.basename(file_name)
            txt_filename = os.path.splitext(basename)[0] + '.txt'
            txt_filepath = os.path.join(CONFIG["input_labels"], txt_filename)

            output_img_path = os.path.join(CONFIG["output_img"],basename)

            subprocess.call('python predict.py ' + CONFIG["cn_model_path"] + ' ' + 
                            CONFIG["config_path"] + ' '+ file_name +
                            ' '+ output_img_path  + ' ' + txt_filepath +
                             ' --img_size ' + CONFIG["cn_input"] )
                        
            print(str(count) + '  complete  ' + basename)

            count +=1
        
    
    else:
        print("mode is not defined")