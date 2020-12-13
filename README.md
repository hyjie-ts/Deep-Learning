# Deep-Learning|paddlepaddle
#我们的项目包含slam、无人机app、腾讯云服务器搭建、云存储、以及人体检测，这部分仅关于飞桨的烟火识别代码
#基于大疆sdk自己开发的APP
```
https://github.com/Magitek-98/DJIUAV
```
#服务器搭建查看
```
ubuntu18.04 搭建Nginx-RTMP视频推流服务器.md
```
##基于paddle飞浆框架使用faster_rcnn_r50_fpn_1x模型进行火灾检测

##训练命令
输出模型保存在output文件中
```
python -u tools/train.py -c configs/faster_rcnn_r50_fpn_1x.yml -o pretrain_weights=faster_rcnn_r50_fpn_1x finetune_exclude_pretrained_params=['cls_score','bbox_pred'] --eval
```
##部署模型
导出模型在inference_model中
```
python -u tools/export_model.py -c configs/faster_rcnn_r50_fpn_1x.yml --output_dir=./inference_model
```
##预测结果
结果在output文件夹中
测试数据在test文件夹中
```
python deploy/python/infer.py --model_dir=./inference_model/faster_rcnn_r50_fpn_1x --image_file=test/44.jpg --use_gpu=True
```
#连接无人机推流
```
python deploy/python/infer_fire.py --model_dir=./inference_model/faster_rcnn_r50_fpn_1x --use_gpu=True
```
