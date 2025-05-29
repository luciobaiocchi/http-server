# Technical Report

## 1. Introduction
The aim of this project was to implement a minimal HTTP server in Python that delivers optimized static content, with advanced MIME type handling, request logging, a responsive interface, and lightweight CSS animations.

## 2. Design Choices
- **Language**: Python 3, for simplicity and rapid prototyping.
- **Sockets**: use of `socket.socket` for low-level TCP communication.
- **Multithreading**: daemon threads to handle concurrent requests without blocking.
- **Logging**: built-in `logging` module writing to a file for post-analysis.

## 3. MIME Type Handling
The server uses `mimetypes.guess_type` to map file extensions to `Content-Type`. It natively supports common extensions:
- **Text**: `.html`, `.css`, `.js`, `.json`, `.txt`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
- **Fonts**: `.woff`, `.woff2`, `.ttf`
- **Others**: `.pdf`, `.zip`, `.xml`

## 4. Request Logging
Logged details include:
- Timestamp in ISO 8601 format.
- Log level (INFO, WARNING, ERROR).
- Request details (client address, method, path).
- Response code and MIME type.
This data supports debugging, usage metrics, and monitoring.

## 5. Responsive Design & CSS Animations
- **Grid Layout**: CSS Grid with `auto-fit` and `minmax` for fluid adaptation.
- **Animations**: fade-in for content and slide-in for the header.
- **Transitions**: hover effects on links and cards with smooth transforms.
- **Breakpoints**: optimized for mobile (< 768px) and tablet.

## 6. Testing & Validation
- Manual testing on Chrome, Firefox, and Edge.
- HTML/CSS validation via the W3C Validator.
- Concurrency testing with ApacheBench (`ab`): 100 concurrent requests, average latency < 50 ms on a local environment.

## 7. Performance & Optimizations
- **Keep-Alive**: future support for `Connection: keep-alive` to reduce TCP overhead.
- **Caching**: add `Cache-Control` headers for static assets.
- **Minification**: compress CSS/JS to reduce file sizes.

## 8. Security & Limitations
- **Directory Traversal**: sanitization of `path` via `lstrip('/')` and `os.path.isfile` checks.
- **Supported Methods**: only GET; other methods (POST, PUT, etc.) are rejected.
- **SSL/TLS**: not implemented; recommend using `stunnel` or an Nginx reverse proxy for HTTPS.

## 9. Future Enhancements
- POST handling and RESTful API support.
- Basic HTTP authentication.
- Real-time monitoring (WebSocket interface).
- Admin dashboard for viewing logs.

## 10. Conclusion
This minimal server meets the core requirements and optional extensions. Its modular design makes it straightforward to add new features such as caching, HTTPS, or API endpoints.
