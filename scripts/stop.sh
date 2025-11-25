#!/bin/bash
docker stop myapp || true
docker rm myapp || true
