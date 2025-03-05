SHELL:=/bin/bash

.SILENT: tf-get
.SILENT: tf-set-workspace

ifneq ("$(wildcard local.env)","")
  include local.env
endif

export SERVICE_NAME=service
export HOSTED_ZONE=service.xyz
export ARTEFACT_BUCKET_NAME := ${SERVICE_NAME}-${ENV}-build-artefacts
export BUILD_VERSION := 1.0.0
export BASE_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

define SET_TF_VARS
	$(eval export TF_VAR_env := ${ENV})
	$(eval export TF_VAR_build_version := ${BUILD_VERSION})
	$(eval export TF_VAR_service_name := ${SERVICE_NAME})
	$(eval export TF_VAR_hosted_zone := ${HOSTED_ZONE})
	$(eval export TF_VAR_base_dir := ${BASE_DIR})
endef

component ?= api

build:
	rm -rf deploy
	pdm export --without-hashes --without test -o requirements.txt
	pip3 install -r requirements.txt --platform manylinux2014_x86_64 --target ./deploy/api --only-binary=:all:
	- cp -a packages/api/src/. deploy/api

start-api:
	cd ./packages/api/src && uvicorn main:app --reload --port=8082

