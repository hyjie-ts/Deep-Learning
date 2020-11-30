# Deep-Learning
#基于paddle飞浆框架使用faster_rcnn_r50_fpn_1x模型进行火灾检测

#训练命令，输出模型保存在output文件中
```
python -u tools/train.py -c configs/faster_rcnn_r50_fpn_1x.yml -o pretrain_weights=faster_rcnn_r50_fpn_1x finetune_exclude_pretrained_params=['cls_score','bbox_pred'] --eval
```
#部署模型，导出模型在inference_model中
```
python -u tools/export_model.py -c configs/faster_rcnn_r50_fpn_1x.yml --output_dir=./inference_model
```
#预测结果，结果在output文件夹中
#测试数据在test文件夹中
```
python deploy/python/infer.py --model_dir=./inference_model/faster_rcnn_r50_fpn_1x --image_file=test/44.jpg --use_gpu=True
```
#连接无人机推流
python deploy/python/infer_fire.py --model_dir=./inference_model/faster_rcnn_r50_fpn_1x --use_gpu=True
