function chime({ gain, duration }) {
    let c = new AudioContext();
    let g = c.createGain();
    let o = c.createOscillator();
    let of = o.frequency;
    g.connect(c.destination)
    g.gain.value = gain;
    g.gain.linearRampToValueAtTime(0, duration)
    o.connect(g)
    o.type = "square";
    of.setValueAtTime(988,0)
    of.setValueAtTime(1319,0.08)
    o.start()
    o.stop(duration)
}
function render({ model, el }) {
    let size = () => `${model.get("size")}px`;
    let canvas = document.createElement("canvas");
    canvas.width = 16;
    canvas.height = 16;
    canvas.style.width = size();
    canvas.style.height = size();
    let bytes = new Uint8ClampedArray(
        model.get("_box").buffer
    );
    let imgData = new ImageData(bytes, 16, 16);
    let ctx = canvas.getContext("2d");
    ctx.putImageData(imgData, 0, 0);

    canvas.addEventListener("click", () => {
        chime({
            gain: model.get("gain"),
            duration: model.get("duration"),
        });
        if (model.get("animate")) {
            canvas.style.animation = "none";
            setTimeout(() => {
                canvas.style.animation = "ipymario-bounce 0.2s";
            }, 10);
        }
    });
    model.on("msg:custom", (msg) => {
        if (msg?.type === "click") canvas.click();
    })
    model.on("change:size", () => {
        canvas.style.width = "30px";
        canvas.style.height = "30px";
    });

    el.classList.add("ipymario");
    el.appendChild(canvas);
}
export default { render };
