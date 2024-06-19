// maps Unity's key inputs to JS equivalent
// will be implemented by parsing through files and changing C# to this

class UnityInput {
    static keys = {};
    static mouseButtons = {};
    static touches = [];

    static initialize() {
        document.addEventListener('keydown', (event) => {
            Input.keys[event.key] = true;
        });

        document.addEventListener('keyup', (event) => {
            Input.keys[event.key] = false;
        });

        document.addEventListener('mousedown', (event) => {
            Input.mouseButtons[event.button] = true;
        });

        document.addEventListener('mouseup', (event) => {
            Input.mouseButtons[event.button] = false;
        });

        document.addEventListener('touchstart', (event) => {
            Input.touches = event.touches;
        });

        document.addEventListener('touchend', (event) => {
            Input.touches = event.touches;
        });

        document.addEventListener('touchmove', (event) => {
            Input.touches = event.touches;
        });
    }

    static GetKey(key) {
        return Input.keys[key] || false;
    }

    static GetMouseButton(button) {
        return Input.mouseButtons[button] || false;
    }

    static GetAxis(axis) {
        if (axis === "Horizontal") {
            return (Input.GetKey('ArrowRight') ? 1 : 0) - (Input.GetKey('ArrowLeft') ? 1 : 0);
        } else if (axis === "Vertical") {
            return (Input.GetKey('ArrowUp') ? 1 : 0) - (Input.GetKey('ArrowDown') ? 1 : 0);
        }
        return 0;
    }

    static touchCount() {
        return Input.touches.length;
    }
}

// Initialize input handling
UnityInput.initialize();
