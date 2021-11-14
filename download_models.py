"""
download_models.py

downloads the model files needed to run things in this repo. If things change just update the folder name and the links
All model files (that have been generated by Peter) are in this dropbox folder:

https://www.dropbox.com/sh/e2hbxkzu1e4vtte/AACdUHz-J735F5Cn-KV4udlka?dl=0
"""

import argparse
import utils
from pathlib import Path
import pprint as pp
from utils import get_timestamp

model_links = {
    "gpt335M_275ks_checkpoint": "https://www.dropbox.com/sh/7kyoo9462lykfhp/AACbtz0FpwEvD24J04n53LGca?dl=1",
    "gpt335M_325ks_checkpoint": "https://www.dropbox.com/sh/5qhujccnpr9b8ba/AABTU9V3N87iYy7qwWEDVfnsa?dl=1",
    "gpt-neo-125M_150ks_checkpoint": "https://www.dropbox.com/sh/e2hbxkzu1e4vtte/AACdUHz-J735F5Cn-KV4udlka?dl=1",
    "gpt2_std_gpu_774M_120ksteps": "https://www.dropbox.com/sh/f8pocv18n0bohng/AACVMXcWR9Kn_CQsZKqpF1xoa?dl=1",
    "gpt2_dailydialogue_355M_75Ksteps": "https://www.dropbox.com/sh/ahx3teywshods41/AACrGhc_Qntw6GuX7ww-3pbBa?dl=1",
    "GPT2_dailydialogue_355M_150Ksteps": "https://www.dropbox.com/sh/nzcgavha8i11mvw/AACZXMoJuSfI3d3vGRrT_cp5a?dl=1",
    "GPT2_trivNatQAdailydia_774M_175Ksteps": "https://www.dropbox.com/sh/vs848vw311l04ah/AAAuQCyuTEfjaLKo7ipybEZRa?dl=1",
    "gp2_DDandPeterTexts_774M_73Ksteps": "https://www.dropbox.com/sh/bnrwpqqh34s2bea/AAAfuPTJ0A5FgHeOJ0cMlUFha?dl=1",
}

# Set up the parsing of command-line arguments
def get_parser():
    parser = argparse.ArgumentParser(
        description="downloads model files if not found in local working directory"
    )
    parser.add_argument(
        "--download-all",
        default=False,
        action="store_true",
        help="pass this argument if you want all the model files instead of just the 'primary' ones",
    )
    parser.add_argument(
        "--verbose",
        default=False,
        action="store_true",
        help="increases amount of printing info to console",
    )

    return parser


if __name__ == "__main__":

    args = get_parser().parse_args()
    get_all = args.download_all
    verbose = args.verbose
    cwd = Path.cwd()
    my_cwd = str(cwd.resolve())  # string so it can be passed to os.path() objects
    print(f"using {my_cwd} as the working directory to store/check models\n")
    folder_names = [str(p.resolve()) for p in cwd.iterdir() if p.is_dir()]
    if verbose:
        print("folder names are as follows: \n")
        pp.pprint(folder_names, compact=True, indent=4)
    if get_all:
        # download model files not as useful (skipped by default)

        m_name = "gpt2_325k_checkpoint"
        if not any(m_name in dir for dir in folder_names):
            # standard GPT-2 trained in a mediocre way up to 325,000 steps on my whatsapp data
            print(f"did not find {m_name} in folders, downloading..")
            extr_loc = cwd / m_name
            model_dest = str(extr_loc.resolve())
            utils.get_zip_URL(
                model_links[m_name],
                extract_loc=model_dest,
                verbose=verbose,
            )
        m_name = "GPT2_dailydialogue_355M_150Ksteps"
        if not any(m_name in dir for dir in folder_names):
            # "DailyDialogues 355M parameter model - to be trained further with custom data or used directly
            print(f"did not find {m_name} in folders, downloading..")
            extr_loc = cwd / m_name
            model_dest = str(extr_loc.resolve())

            utils.get_zip_URL(
                model_links[m_name],
                extract_loc=model_dest,
                verbose=verbose,
            )

        if verbose:
            print(
                "finished downloading optional model files - {ts}".format(
                    ts=get_timestamp()
                )
            )

    # TODO: turn these into functions
    m_name = "GPT2_trivNatQAdailydia_774M_175Ksteps"
    if not any(m_name in dir for dir in folder_names):
        # base "advanced" 774M param GPT-2 model trained on: Trivia, Natural Questions, Daily Dialogues
        print(f"did not find {m_name} in folders, downloading..")
        extr_loc = cwd / m_name
        model_dest = str(extr_loc.resolve())
        utils.get_zip_URL(
            model_links[m_name],
            extract_loc=model_dest,
            verbose=verbose,
        )

    m_name = "gp2_DDandPeterTexts_774M_73Ksteps"
    if not any(m_name in dir for dir in folder_names):
        # GPT-Peter: trained on 73,000 steps of Peter's messages in addition to same items as GPT2_trivNatQAdailydia_774M_175Ksteps
        print(f"did not find {m_name} in folders, downloading..")
        extr_loc = cwd / m_name
        model_dest = str(extr_loc.resolve())
        utils.get_zip_URL(
            model_links[m_name],
            extract_loc=model_dest,
            verbose=verbose,
        )

    print("finished downloading and checking files {ts}".format(ts=get_timestamp()))
