console.log("Script cargado");
import { codes } from "./codes.js";

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contacto-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        
        const nombre = document.getElementById("nombre").value;
        const email = document.getElementById("email").value;
        const mensaje = document.getElementById("mensaje").value;

        if (nombre && email && mensaje) {
            alert(`¡Gracias, ${nombre}! Tu mensaje ha sido enviado.`);
            form.reset();
        } else {
            alert("Por favor, completa todos los campos.");
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const codeArea = document.getElementById("code");

    window.loadCode = function (index) { // <-- Hacemos la función accesible globalmente
        if (codes[index] !== undefined) {
            codeArea.value = codes[index];
        }
    };
});

document.addEventListener("DOMContentLoaded", function () {
    const codeArea = document.getElementById("code");
    const outputElement = document.getElementById("outputweb");

    window.runPython = async function () {
        let code = codeArea.value.trim();
        if (!code) {
            outputElement.innerText = "No hay código para ejecutar.";
            return;
        }
    
        if (!outputElement) {
            console.error("❌ ERROR: No se encontró el elemento con id='outputweb'");
            return;
        }
    
        try {
            if (!window.pyodide) {
                window.pyodide = await loadPyodide();
            }
    
            await window.pyodide.runPythonAsync(`
                import sys
                from io import StringIO
                sys.stdout = StringIO()
                sys.stderr = sys.stdout
            `);
    
            await window.pyodide.runPythonAsync(code);
    
            let output = await window.pyodide.runPythonAsync("sys.stdout.getvalue()");
            outputElement.innerText = output || "Salida vacía";
    
        } catch (error) {
            console.error("Error ejecutando Python:", error);
            outputElement.innerText = `Error: ${error.message}`;
        }
    };
});

async function loadPyodideAndCheck() {
    console.log("Cargando Pyodide...");
    window.pyodide = await loadPyodide();
    console.log("Pyodide cargado correctamente.");
}

loadPyodideAndCheck();

const foto = document.getElementById('fotoPerfil');
const modal = document.getElementById('modal');
const closeModal = document.getElementById('closeModal');

foto.onclick = function() {
    modal.style.display = "flex";
}

closeModal.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
