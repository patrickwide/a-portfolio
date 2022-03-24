document.addEventListener('DOMContentLoaded', () => {
    var canvas = document.querySelector('#canvas');
    var ctx = canvas.getContext('2d');


    function resize(){
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
    }

    window.addEventListener('resize',resize());

    let painting = false;

    function startPosition(e){
        painting = true;
        draw(e);
    }
    function finishedPosition(){
        painting = false;
        ctx.beginPath();
    }

    function draw(e){
        if(!painting) return;
        ctx.lineWidth = 4;
        ctx.lineCap = "round";

        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX,e.clientY);
    }
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', finishedPosition);
    canvas.addEventListener('mousemove', draw);




    alert(ctx);
    return false;

});
