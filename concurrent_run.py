import datetime
import os
import threading

def execCmd(cmd):
    try:
        print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        os.system(cmd)
        print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except:
        print('%s\t 运行失败' % (cmd))


if __name__ == '__main__':
    # 是否需要并行运行
    if_parallel = True

    # 需要执行的命令列表
    base_command = "python inference.py --checkpoint_path ./checkpoints/Wav2Lip_GAN.pth --face ../inputs/train_close_mouth_480p.mp4 --audio ../inputs/test.wav --outfile results/result_voice_{}.mp4"
    # base_command = "python run.py -output_file results/result_voice_{}.mp4"
    num_threads = 4  # 1, 2, 4, 6, 8, 10, 12

    commands = [
        base_command.format(i) for i in range(num_threads)
    ]

    # print(commands)

    if if_parallel:
        # 并行
        threads = []
        for cmd in commands:
            th = threading.Thread(target=execCmd, args=(cmd,))
            th.start()
            threads.append(th)

        # 等待线程运行完毕
        for th in threads:
            th.join()
    else:
        # 串行
        for cmd in commands:
            try:
                print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
                os.system(cmd)
                print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
            except:
                print('%s\t 运行失败' % (cmd))