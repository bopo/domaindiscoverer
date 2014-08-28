/*
 Navicat Premium Data Transfer

 Source Server         : data
 Source Server Type    : SQLite
 Source Server Version : 3008004
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008004
 File Encoding         : utf-8

 Date: 08/28/2014 14:50:59 PM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for pinyin_domains
-- ----------------------------
DROP TABLE IF EXISTS "pinyin_domains";
CREATE TABLE "pinyin_domains" (
	 "word" text NOT NULL,
	 "pinyin" TEXT NOT NULL,
	 "frequency" integer,
	 "available_com" TEXT,
	 "available_cn" TEXT,
	 "expiry_date_com" TEXT,
	 "expiry_date_cn" TEXT,
	 "last_updated" text,
	PRIMARY KEY("word")
);

PRAGMA foreign_keys = true;
