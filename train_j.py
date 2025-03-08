import argparse
import os
from traintrain.trainer.train import train_main
from traintrain.trainer.trainer import import_json
import traintrain.scripts.traintrain

def main():
    parser = argparse.ArgumentParser(description="Load and display JSON file content.")
    
    parser.add_argument("json_path", type=str, help="Path to the JSON file")
    parser.add_argument("--models-dir", type=str, default=None, help="Directory for models")
    parser.add_argument("--ckpt-dir", type=str, default=None, help="Directory for StableDiffusion Models (overrides --models-dir)")
    parser.add_argument("--vae-dir", type=str, default=None, help="Directory for VAE (overrides --models-dir)")
    parser.add_argument("--lora-dir", type=str, default=None, help="Directory for LoRA (overrides --models-dir)")
    
    args = parser.parse_args()
    paths = [args.models_dir, args.ckpt_dir, args.vae_dir, args.lora_dir]
    
    inputs = import_json(args.json_path, cli = True)
    print(inputs)
    result = train_main(paths, *inputs)
    print(result)

if __name__ == "__main__":
    main()