# video-to-text
a program who creates .mp4 text videos (muted)



step 1 - path to file

step 2 - frames per second (input shold be float between 1 and 0.infinity)

step 3 - output name

step 4 - colors: "y" will make a grid of 6x6 pixels (dots) and they will have a color, anything else will make the same, but whiout color


ps: if you have a file named frames, don't run in the same directory, all of its contents will be deleted (for video creation we stract images and then edit they)
and the program is not threaded, so it can take a while to end.

# threaded version
step 1 - path to file

step 2 - frames per second (input shold be float between 1 and 0.infinity)

step 3 - max threads

step 4 - output name

step 5 - colors: "y" will make a grid of 6x6 pixels (dots) and they will have a color, anything else will make the same, but whiout color


#about fps:

the fps float works as a division for the frames, how lower, is how much frame per second you will get
example: 0.0069 you will get around 144 frames per second, because 1 / 0.0069 gives the same result.