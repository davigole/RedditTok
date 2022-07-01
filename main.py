import click
from random import randint

from master.console import create_log
from master.audio import concatenate_audios
from master.utils import create_temp, delete_dir
from master.reddit import create_driver, check_nsfw, set_darkmode, get_comments, get_title
from master.background import load_background, crop_video, remove_audio
from master.video import add_audio, add_data

@click.command()
@click.argument("url")
@click.option("--path", help="Path for final video", default="output.mp4")
@click.option("--comments", help="Maximum number of comments", default=5)
@click.option("--background_path", help="Path for background video", default="assets/background.mp4")
@click.option("--background_start", help="Moment in seconds when background video starts (leave empty for random)", default=-1)
@click.option("/L", help="Set Reddit screenshots to light mode", is_flag=True)
@click.option("/T", help="Keep temporary files after execution", is_flag=True)
def main(url: str, path: str, comments: int, background_path: str, background_start: int, l: bool, t: bool):
    log = create_log()

    # Create temp folder
    create_temp()
    log.info("Created temp folder")


    # Get Reddit screenshots and audios
    driver = create_driver(url)

    if check_nsfw(driver):
        log.info("NSFW alert dismissed")

    if not l:
        set_darkmode(driver)
        log.info('Set Reddit to dark mode')
    
    title_data = get_title(driver)
    comments_data = get_comments(driver, n=comments)

    if len(comments_data) < comments: log.warning("{} comments found. {} wanted".format(len(comments_data), comments))

    data = [title_data] + comments_data
    log.info("Title and comments data found")

    driver.close()
    driver.quit()

    
    # Concatenate audios into one
    final_audio = concatenate_audios([i['audio'] for i in data])
    log.info('Concatenated audios into one')
    
    # Load background video
    background_video = load_background(background_path)
    log.info("Loaded background video")
    
    maximum_start = int(background_video.duration) - int(final_audio.duration)

    if background_start > maximum_start:
        background_start = maximum_start
        log.critical("Background start should be at most {} but is {}. Changed it to {}".format(
            maximum_start, background_start, maximum_start
        ))
    elif background_start == -1:
        background_start = randint(0, maximum_start)
        log.info("Background start was randomized to {}".format(background_start))

    background_end = background_start + final_audio.duration
    background_video = crop_video(background_video, background_start, background_end)
    log.info('Cropped background video from {} to {}'.format(background_start, background_end))

    background_video = remove_audio(background_video)
    log.info('Removed sound from background video')

    background_video = add_audio(background_video, final_audio)
    log.info('Added text-to-speech audio to background video')

    background_video = add_data(background_video, data)
    log.info('Added data to background video')

    
    # Export video
    log.info('The final video has a duration of {} seconds'.format(int(background_video.duration)))
    if background_video.duration > 180: log.warning('TikTok videos can be up to 180 seconds long and final video has {} seconds'.format(int(background_video.duration)))

    background_video.write_videofile(path)
    log.info('Exported background_video to {}'.format(path))
    

    # Delete temp folder
    if not t:
        try:
            delete_dir('temp')
            log.info('Deleted temp folder')
        except PermissionError:
            log.warning('Temp folder cannot be deleted because it is being used by another process')
    

if __name__ == '__main__':
    main()