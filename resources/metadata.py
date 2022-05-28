"""
Part of the code that I used to generate the metadata for my NFT collection.
"""

import json


class MindBlockMetadata():

    def __init__(self, text, line, num, ipfs_url):
        self.number =  num
        self.person = 'patient' if 'patient' in text else 'antropologist'
        self.sentence = line
        self.learning_rate = text.split('_')[-2].split(' ')[0]
        self.steps = text.split('_')[-1].split('.')[0].split('-')[0]
        self.image_ipfs_url = f'https://{ipfs_url}.ipfs.nftstorage.link/images/{num}.jpg'
        self.name = f'MindBlock #{num}'



def create_metadata(metadata):
    """
    Creates the metadata json file with MindBlockMetadata object
    """

    metadata_structure = {
        "attributes": [
            {
            "trait_type": "who said it",
            "value": metadata.person
            },
            {
            "trait_type": "prompt",
            "value": metadata.sentence
            },
            {
            "trait_type": "learning rate:",
            "value": metadata.learning_rate
            },
            {
            "trait_type": "steps:",
            "value": metadata.steps
            }
        ],

        "description": f'"{metadata.sentence}"\n\nHow do we approach the task of constructing a shared view of reality when trust is decentralized, truth is minted, and the growing set of global challenges requires us to collaborate with those whose cultural context and perceptions may diverge from our own? Can applying large pretrained text-to-image neural networks to generate visual metaphors suggest a way forward?\n\nThis image is one of 109 in the inaugural MindBlock.art collection and was generated using a prompt from transcribed utterances encoded using OpenAI CLIP and through a shared representation, used to drive generation of images you see. [1] The prompts come from some of the first patients with schizophrenia to be studied at the Palo Alto Mental Research Institute, as well as from the interpretations of the researchers studying them. [2]  [3]\n\nModel: https://github.com/openai/CLIP \nWeights: ViT-B-32\nCode: https://github.com/ombrusco/mindblock \n\nConnect with us https://twitter.com/MindBlockArt 🧠 \n\nReferences\n1. "Learning Transferable Visual Models From Natural Language Supervision" Radford et al (2021) 10.48550/arXiv.2103.00020 \n2. "Toward a Theory of Schizophrenia" Bateson, Jackson et al (1956)  10.1002/bs.3830010402 \n3. "On Human Communication" Watzlawick, Jackson (1964) 10.1521/jsyt.2010.29.2.53',
        "external_url": 'https://www.mindblock.art/',
        "image": metadata.image_ipfs_url,
        "name": metadata.name
    }
    
    with open(f'metadata/{metadata.number}', 'w') as outfile:
        json.dump(metadata_structure, outfile)