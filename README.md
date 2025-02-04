## Media
### Rendering commands
`ffmpeg -i LorenzAttractor.mp4 -vf "fps=30,scale=-1:720:flags=lanczos" -c:v gif LorenzAttractor720p30fps.gif*`  
`ffmpeg -i LorenzAttractor.mp4 -vf "fps=30,scale=-1:1080:flags=lanczos" -c:v gif LorenzAttractor1080p30fps.gif*`
### Lorenz Attractor
![Lorenz Attractor](media/LorenzAttractor720p30fps.gif)
