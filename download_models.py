"""
download_models.py

downloads the model files needed to run things in this repo. If things change just update the folder name and the links. Note that model files are between 1.5 - 5 gb, and can take a while to download.

All model files (that have been generated by Peter) are in this dropbox folder:

https://www.dropbox.com/sh/e2hbxkzu1e4vtte/AACdUHz-J735F5Cn-KV4udlka?dl=0
"""

import argparse
import utils
from pathlib import Path
import pprint as pp
from utils import get_timestamp

model_links = {
    "gpt2_dailydialogue_355M_75Ksteps": "https://www.dropbox.com/sh/ahx3teywshods41/AACrGhc_Qntw6GuX7ww-3pbBa?dl=1",
    "GPT2_dailydialogue_355M_150Ksteps": "https://www.dropbox.com/sh/nzcgavha8i11mvw/AACZXMoJuSfI3d3vGRrT_cp5a?dl=1",
    "GPT2_trivNatQAdailydia_774M_175Ksteps": "https://www.dropbox.com/sh/vs848vw311l04ah/AAAuQCyuTEfjaLKo7ipybEZRa?dl=1",
    "gp2_DDandPeterTexts_774M_73Ksteps": "https://www.dropbox.com/sh/bnrwpqqh34s2bea/AAAfuPTJ0A5FgHeOJ0cMlUFha?dl=1",
    "GPT2_WoW_100k_genconv_355M": "https://www.dropbox.com/sh/5hvgjgmpy5ucq4t/AAAITp8gTjiilla1Q7lvX_2ua?dl=1",
    "GPTneo_conv_33kWoW_18kDD": "https://www.dropbox.com/sh/dfb3v40dn2ubgqq/AADeRBZ1agCOy4SNcGBfiP2fa?dl=1",
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
        help="pass this argument if you want most of the model files instead of just the 'primary' ones",
    )
    parser.add_argument(
        "--gpt-whatsapp",
        default=False,
        action="store_true",
        help="pass this argument if you want a model trained on the WhatsApp dataset",
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
    get_whatsapp_example = args.gpt_whatsapp
    verbose = args.verbose
    cwd = Path.cwd()
    my_cwd = str(cwd.resolve())  # string so it can be passed to os.path() objects
    print(f"using {my_cwd} as the working directory to store/check models\n")
    folder_names = [str(p.resolve()) for p in cwd.iterdir() if p.is_dir()]
    if verbose:
        print("folder names are as follows: \n")
        pp.pprint(folder_names, compact=True, indent=4)
    if get_all:
        # download model files not as important (skipped by default to reduce D/L time)

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
            
        m_name = "GPT2_WoW_100k_genconv_355M"
        if not any(m_name in dir for dir in folder_names):
            # GPT2_WoW_100k_genconv_355M: pretrained GPT-2 fine-tuned on wizard of wikipedia dataset for 100k steps
            print(f"did not find {m_name} in folders, downloading..")
            extr_loc = cwd / m_name
            model_dest = str(extr_loc.resolve())
            utils.get_zip_URL(
                model_links[m_name],
                extract_loc=model_dest,
                verbose=verbose,
            )

        m_name = "GPTneo_conv_33kWoW_18kDD"
        if not any(m_name in dir for dir in folder_names):
            # GPTneo_conv_33kWoW_18kDD: GPT-Neo 1.3B finetuned on wizard of wikipedia dataset for 33k steps and 18k steps on daily dialogue
            # this file is ~ 5 GB!
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
            
    if get_whatsapp_example:

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

    # TODO: turn these into functions
    m_name = "GPT2_trivNatQAdailydia_774M_175Ksteps"
    if not any(m_name in dir for dir in folder_names):
        # base "advanced" 774M param GPT-2 model trained on: Trivia, Natural Questions, Daily Dialogues for a total of 175,000 steps
        print(f"did not find {m_name} in folders, downloading..")
        extr_loc = cwd / m_name
        model_dest = str(extr_loc.resolve())
        utils.get_zip_URL(
            model_links[m_name],
            extract_loc=model_dest,
            verbose=verbose,
        )

   
    print("finished downloading and checking files {ts}".format(ts=get_timestamp()))
