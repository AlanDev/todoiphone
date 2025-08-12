import { exec } from 'child_process';
import { writeFileSync, readFileSync } from 'fs';
import { promisify } from 'util';

const execAsync = promisify(exec);

export default async function handler(req, res) {
  // Solo permitir POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    console.log('🔄 Starting data update...');
    
    // Ejecutar el scraper Python
    const { stdout, stderr } = await execAsync('python simple_scraper.py');
    
    if (stderr) {
      console.error('❌ Error:', stderr);
      return res.status(500).json({ error: 'Scraper failed', details: stderr });
    }
    
    console.log('✅ Scraper output:', stdout);
    
    // Leer el CSV actualizado
    const csvData = readFileSync('iphone_prices.csv', 'utf8');
    
    // Contar productos
    const lines = csvData.split('\n').filter(line => line.trim());
    const productCount = lines.length - 1; // -1 por el header
    
    console.log(`📊 Updated ${productCount} products`);
    
    res.status(200).json({
      success: true,
      message: 'Data updated successfully',
      productCount,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('❌ Error updating data:', error);
    res.status(500).json({ 
      error: 'Failed to update data',
      details: error.message 
    });
  }
} 