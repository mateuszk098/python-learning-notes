from time import sleep

from rich.progress import Progress, BarColumn, TimeElapsedColumn, SpinnerColumn

progress = Progress(
    TimeElapsedColumn(),
    '[magenta]{task.description}',
    BarColumn(),
    '[magenta]Step {task.completed} of {task.total}',
    SpinnerColumn(),
)

with progress:
    task = progress.add_task("Processing..", total=10)
    for n in range(10):
        sleep(0.5)
        progress.update(task, advance=1)

    # basewidth = 25
    # img = Image.open('arrow.png')
    # wpercent = (basewidth/float(img.size[0]))
    # hsize = int((float(img.size[1])*float(wpercent)))
    # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img.save('somepic.png')

    # arrow_up = Image.open('arrow_u.png')
    # arrow_down = Image.open('arrow_d.png')
    # width, height = arrow_up.size

    # n = 10   # paste image n-times

    # # set width, height of new image based on original image
    # img = Image.new('RGB', (width*n, height*n))
    # img.save('out.png')

    # for i in range(0, n):
    #     for j in range(0, n):
    #         out = Image.open('out.png')
    #         # the second argument here is tuple representing upper left corner
    #         if i % 2 == 0:
    #             out.paste(arrow_up, (i*width, j*height))
    #         else:
    #             out.paste(arrow_down, (i*width, j*height))
    #         out.save('out.png')
