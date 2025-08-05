# Simple Flask E‑Commerce Demo

A minimal e‑commerce application built with Flask for learning/demo purposes.

## Overview

This small-scale demo allows users to:
- Browse a set of sample products
- Add items to a session-based cart
- View a cart summary and total
- Simulate a checkout process (clearing the cart)

Everything runs in memory, without a database, making it ideal for experimentation.

## Features

- Static product catalog defined in `example.py`
- Cart handled via Flask session
- Basic routing and templates using `render_template_string`
- Dummy checkout clears cart and displays a thank-you message

## Requirements

- Python 3.x
- Flask

Install dependencies:

```bash
pip install Flask
# E-commerce-example.py
