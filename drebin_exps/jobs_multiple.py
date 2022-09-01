#!/bin/sh


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_adam_0.001_batch_16_bn_drop_multihead 



echo $'############ START Task-IL ############'
now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_sgd_0.01_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_sgd_0.01_batch_16_multihead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_adam_0.001_batch_16_multihead

now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=current --distill --exp_name LwF_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=current --distill --exp_name LwF_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_adam_0.001_batch_16_multihead

python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_sgd_0.01_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_sgd_0.01_batch_16_multihead




now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_adam_0.001_batch_16_multihead

python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_sgd_0.01_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_sgd_0.01_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --lambda=5000 --exp_name EWC_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --lambda=5000 --exp_name EWC_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --online --lambda=5000 --gamma=1 --exp_name EWC_online_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --online --lambda=5000 --gamma=1 --exp_name EWC_online_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --si --c=0.1 --exp_name SI_adam_0.001_batch_16_singlehead --singlehead

python main.py --tasks 9 --scenario=task --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --si --c=0.1 --exp_name SI_adam_0.001_batch_16_multihead




echo $'############ START Class-IL ############'
now="$(date)"
printf "Current date and time %s\n" "$now"
python main.py --tasks 9 --scenario=class --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=none --exp_name none_sgd_0.01_batch_16_multihead

python main.py --tasks 9 --scenario=class --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_sgd_0.01_batch_16_multihead

python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=none --exp_name none_adam_0.001_batch_16_multihead

python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=offline --exp_name offline_adam_0.001_batch_16_multihead

now="$(date)"
printf "Current date and time %s\n" "$now"

python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=current --distill --exp_name LwF_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_adam_0.001_batch_16_multihead


python main.py --tasks 9 --scenario=class --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --exp_name GR_sgd_0.01_batch_16_multihead




now="$(date)"
printf "Current date and time %s\n" "$now"


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_adam_0.001_batch_16_multihead


python main.py --tasks 9 --scenario=class --lr=0.01 --optimizer=sgd --batch 32 --pdf --logger_file drebin --replay=generative --distill --exp_name GR_distill_sgd_0.01_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --lambda=5000 --exp_name EWC_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --ewc --online --lambda=5000 --gamma=1 --exp_name EWC_online_adam_0.001_batch_16_multihead



now="$(date)"
printf "Current date and time %s\n" "$now"


python main.py --tasks 9 --scenario=class --lr=0.001 --optimizer=adam --batch 32 --pdf --logger_file drebin --si --c=0.1 --exp_name SI_adam_0.001_batch_16_multihead


