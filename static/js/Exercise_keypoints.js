let capture;
let posenet;
let singlePose;
let skeleton;

function setup()
{
    createCanvas(1066,600);
    capture = createCapture(VIDEO);
    capture.size(1066, 600);
    capture.hide();
    
    capture.parent('main_div');

    posenet = ml5.poseNet(capture, modelLoaded);
    posenet.on('pose',receivedPose);
    
}

function receivedPose(poses)
{
    //console.log(poses.length);

    if (poses.length > 0)
    {
        singlePose = poses[0].pose;
        skeleton =poses[0].skeleton;
    }
}

function modelLoaded()
{   
    console.log("model load vayo");
}

function draw()
{ 
    image(capture,0,0);
    fill(0,255,0);

    if(singlePose)
    {
        for(let i=0; i< singlePose.keypoints.length; i++){
            tempX = singlePose.keypoints[i].position.x;
            tempY = singlePose.keypoints[i].position.y;
            ellipse(tempX, tempY, 20);       
        }
        stroke(255,255,255);
        strokeWeight(5);
        for(let j=0; j<skeleton.length; j++){
            line(skeleton[j][0].position.x, skeleton[j][0].position.y, skeleton[j][1].position.x, skeleton[j][1].position.y)
        }

    }
   
    
}