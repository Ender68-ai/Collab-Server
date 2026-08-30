const http = require("http");
const fs = require("fs");

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        const html = fs.readFileSync("index.html");

        res.writeHead(200, {
            "Content-Type": "text/html"
        });

        res.end(html);
        return;
    }

    res.writeHead(404);
    res.end("404 Not Found");
});

server.listen(8001, "0.0.0.0", () => {
    console.log("MPEdit web server running on port 8001");
}); 