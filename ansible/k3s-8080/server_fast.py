import sys
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get(f"/{sys.argv[2]}")
def read_root():
    return f"Hello World ({sys.argv[2]})"

def main(port):
    uvicorn.run("server_fast:app", host="0.0.0.0", port=port, reload=True)

if __name__ == '__main__':
    main(int(sys.argv[1]))
