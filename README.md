# HilbertLib  

A versatile Python library providing tools for **bot development**, **mathematics**, **web utilities**, **color manipulation**, and **database interactions**.

---  
## 📦 Installation  
```bash  
pip install hilbertlib  
```  

---  
## 🛠 Features  

### 🤖 **Bot Development**  
- `DiscordBot` – Framework for Discord bots  
- `TelegramBot` – Tools for Telegram bots  
- `ChatBot` – General-purpose chatbot  

### ➗ **Math Tools**  
- **Vectors**: `Vector2D`, `Vector3D`  
- **Matrices**: `Matrix2D`, `Matrix3D`  
- **Interpolation**: `Polynomial`, `Interpolator`  
- **Probability**: `NormalDistribution`, `UniformDistribution`, `BinomialDistribution`, etc.  
- **Statistics**: `Statistics`  
- **Tensors**: `Tensor`  

### 🌐 **Web Utilities**  
- `APIHandler` – Simplified API interactions  
- `WebScraper` – Data extraction from websites  
- `ProxyManager` – Proxy handling  
- `RateLimiter` – Request throttling  
- `Webhook` – Webhook support  

### 🎨 **Colors**  
- `RGBMixer` – Blend RGB colors  
- `RandomColorGenerator` – Generate random colors  
- `ColorConverter` – Convert between color formats  

### 🗃 **Database**  
- `MySQLHelper` – MySQL database operations  
- `SQLiteHelper` – SQLite database helper  
- `HilbertBasicDB` – Simple key-value storage  

---  
## 📖 Usage Examples  
See the **[examples folder](./examples/)** for detailed usage.  

### Basic Math Example  
```python  
from hilbertlib.math_tools.vectors import Vector3D  

v1 = Vector3D(1, 2, 3)  
v2 = Vector3D(4, 5, 6)  
print(v1 + v2)  # Vector addition  
print(v1.dot(v2))  # Dot product  
```  

### Web Scraping Example  
```python  
from hilbertlib.web_utils.web_scraper import WebScraper  

scraper = WebScraper()  
data = scraper.scrape("https://example.com")  
print(data)  
```  

---  
## 📜 License  
**MIT License**  
Copyright (c) 2025 **Synthfax**  

> 📌 See **[LICENSE](./LICENSE)** for full terms.  

---  
## 🚀 Contributing  
Contributions are welcome! Open an issue or submit a pull request.  

---  
## 👨‍💻 Author  
**Synthfax**
