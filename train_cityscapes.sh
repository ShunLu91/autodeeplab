if [ ! -d logdir  ];then
  mkdir logdir
fi

#CUDA_VISIBLE_DEVICES=6 python train_autodeeplab.py \
# --batch-size 2 --dataset cityscapes --checkname July29_newbetas_branch \
# --alpha_epoch 20 --filter_multiplier 8 --resize 512 --crop_size 321

CUDA_VISIBLE_DEVICES=6 nohup python -u train_autodeeplab.py --batch-size 4 --dataset cityscapes \
 --checkname July29_newbetas_branch --alpha_epoch 20 --filter_multiplier 8 --resize 512 --crop_size 321  > ../logdir/ad0_s.log  2>&1 &

