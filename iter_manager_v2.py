import argparse
import os
import sys
import pandas as pd
from run_search_iteration import run_iter


def main(args):
    rf_step = args.rf_step-1
    filelist = pd.read_csv(args.file)
    #print(filelist[["model_name","model_file"]])
    for index, row in filelist[["model_name","config_str","prec"]].iterrows():
        model_name = row["model_name"]
        config_str = row["config_str"]
        prec = row["prec"]
        output_loc = args.output + row["model_name"]
        for rf in range(args.rf_lower, args.rf_upper, rf_step):
            print("Running hls4ml Synth (vsynth: {}) for {} with RF of {}".format(args.vsynth,model_name, rf))
            run_iter(model_name, output_loc,  rf, args.output, vsynth=args.vsynth, strat=args.hls4ml_strat, precision=prec, config_str=config_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='pregen_3layer_models/filelist.csv')
    parser.add_argument('-u', '--rf_upper', type=int, default=1025)
    parser.add_argument('-l', '--rf_lower', type=int, default=1)
    parser.add_argument('-s', '--rf_step', type=int, default=512)
    parser.add_argument('-o', '--output', type=str, default='./output')
    parser.add_argument("-p", "--prefix", type=str, default='/opt/repo/wa-hls4ml-search/')
    parser.add_argument("-v", "--vsynth", action='store_true')
    parser.add_argument( '--hls4ml_strat', type=str, default="Resource")
    args = parser.parse_args()

    main(args)