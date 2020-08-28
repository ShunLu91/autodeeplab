if [ ! -d logdir  ];then
  mkdir logdir
fi

#************** search **************#
#CUDA_VISIBLE_DEVICES=6 python train_autodeeplab.py \
# --batch-size 2 --dataset cityscapes --checkname July29_newbetas_branch \
# --alpha_epoch 20 --filter_multiplier 8 --resize 512 --crop_size 321

#CUDA_VISIBLE_DEVICES=5 nohup python -u train_autodeeplab.py --batch-size 2 --dataset cityscapes \
# --checkname ad0_s --alpha_epoch 20 --filter_multiplier 8 --resize 512 --crop_size 321  > logdir/ad0_s.log  2>&1 &

#CUDA_VISIBLE_DEVICES=6 nohup python -u train_autodeeplab.py --batch-size 4 --dataset cityscapes \
# --checkname ad1_s --alpha_epoch 20 --filter_multiplier 8 --resize 512 --crop_size 321  > logdir/ad1_s.log  2>&1 &

#************** decode **************#
#CUDA_VISIBLE_DEVICES=6 nohup python -u decode_autodeeplab.py --dataset cityscapes \
#  --resume ./run/cityscapes/ad1_s/experiment_0/checkpoint.pth.tar > logdir/ad1_s_decode.log  2>&1 &

#************** retrain **************#
CUDA_VISIBLE_DEVICES=6 nohup python -u train.py --exp ad1_retrain --dataset cityscapes --workers 8 \
  --net_arch ./run/cityscapes/ad1_s/experiment_0/network_path_space.npy --batch_size 16 \
  --net_path ./run/cityscapes/ad1_s/experiment_0/network_path.npy \
  --cell_arch ./run/cityscapes/ad1_s/experiment_0/genotype.npy > logdir/ad1_retrain.log  2>&1 &
tail -f logdir/ad1_retrain.log