from modules import launch_utils

args = launch_utils.args
prepare_environment = launch_utils.prepare_environment
start = launch_utils.start

def main():
    if args.dump_sysinfo:
        filename = launch_utils.dump_sysinfo()

        print(f"Sysinfo saved as {filename}. Exiting...")

        exit(0)

    if not args.skip_prepare_environment:
        prepare_environment()
    
    import modules.gradio_extensions

    start()

if __name__ == "__main__":
    main()
