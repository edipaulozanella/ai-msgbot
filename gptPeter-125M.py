import gc
import os
import pprint as pp
import time
from datetime import datetime
from os.path import join

from aitextgen import aitextgen

folder_path = join(os.getcwd(), r"gpt-neo_datasetv2/GPT-Neo 125M dataset 2")
verbose=False

if __name__ == "__main__":
    ai = aitextgen(model_folder=folder_path, to_gpu=False,
                   gradient_checkpointing=True)

    print("loaded model - ", datetime.now())

    stay_in_chat = True

    while stay_in_chat:
        user_query = str(input("enter your prompt here (write 'exit' to exit) -->")).lower()
        if user_query == 'exit':
            print("... exiting loop")
            stay_in_chat = False
            break
        st = time.time()
        p_list = []
        p_list.append(user_query + "\n")
        p_list.append("peter szemraj:" + "\n")
        this_prompt = "".join(p_list)
        print("\n... generating... \n")
        this_result = ai.generate(
            n=1,
            top_k=10,
            batch_size=10,
            max_length=64,
            min_length=16,
            prompt=this_prompt,
            temperature=0.7, top_p=0.9, do_sample=True, return_as_list=True,
        )

        this_result = str(this_result[0]).split('\n')
        if verbose: print("the type of the result is {} and length is {}".format(type(this_result),
                                                                                 len(this_result)))

        if len(this_result) > 2:
            output = str(this_result[2]).strip()
        elif isinstance(this_result, list):
            output = str(" ".join(this_result)).strip()
        else:
            output = this_result

        pp.pprint(output, indent=4)
        # pp.pprint(this_result[3].strip(), indent=4)
        rt = round(time.time() - st, 1)
        gc.collect()

        print("took {runtime} seconds to generate. \n".format(runtime=rt))

    print("finished - ", datetime.now())
