#!/usr/bin/env node
/**
 * iPhone Price Scraper - CEBRA
 * Script de inicio para ejecutar la aplicación Streamlit
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🚀 iPhone Price Scraper - CEBRA');
console.log('📱 Iniciando aplicación Streamlit...\n');

// Verificar si Python está instalado
function checkPython() {
    return new Promise((resolve, reject) => {
        const python = spawn('python', ['--version']);
        python.on('close', (code) => {
            if (code === 0) {
                resolve('python');
            } else {
                const python3 = spawn('python3', ['--version']);
                python3.on('close', (code3) => {
                    if (code3 === 0) {
                        resolve('python3');
                    } else {
                        reject(new Error('Python no encontrado. Por favor instala Python 3.9+'));
                    }
                });
            }
        });
    });
}

// Instalar dependencias si es necesario
function installDependencies(pythonCmd) {
    return new Promise((resolve, reject) => {
        console.log('📦 Verificando dependencias...');
        
        try {
            require('streamlit');
            console.log('✅ Streamlit ya está instalado');
            resolve();
        } catch (e) {
            console.log('📥 Instalando dependencias...');
            const pip = spawn(pythonCmd, ['-m', 'pip', 'install', '-r', 'requirements.txt']);
            
            pip.stdout.on('data', (data) => {
                console.log(data.toString());
            });
            
            pip.stderr.on('data', (data) => {
                console.error(data.toString());
            });
            
            pip.on('close', (code) => {
                if (code === 0) {
                    console.log('✅ Dependencias instaladas correctamente');
                    resolve();
                } else {
                    reject(new Error('Error al instalar dependencias'));
                }
            });
        }
    });
}

// Ejecutar la aplicación Streamlit
function runStreamlit(pythonCmd) {
    console.log('🌐 Iniciando servidor web...');
    console.log('📋 La aplicación se abrirá en: http://localhost:8501');
    console.log('🔄 Presiona Ctrl+C para detener el servidor\n');
    
    const streamlit = spawn(pythonCmd, [
        '-m', 'streamlit', 'run', 'app_streamlit.py',
        '--server.port', '8501',
        '--server.address', 'localhost'
    ]);
    
    streamlit.stdout.on('data', (data) => {
        console.log(data.toString());
    });
    
    streamlit.stderr.on('data', (data) => {
        console.error(data.toString());
    });
    
    streamlit.on('close', (code) => {
        console.log(`\n👋 Aplicación cerrada con código: ${code}`);
    });
    
    // Manejar Ctrl+C
    process.on('SIGINT', () => {
        console.log('\n🛑 Deteniendo servidor...');
        streamlit.kill('SIGINT');
        process.exit(0);
    });
}

// Función principal
async function main() {
    try {
        const pythonCmd = await checkPython();
        await installDependencies(pythonCmd);
        runStreamlit(pythonCmd);
    } catch (error) {
        console.error('❌ Error:', error.message);
        process.exit(1);
    }
}

// Ejecutar si es el script principal
if (require.main === module) {
    main();
}

module.exports = { main };
