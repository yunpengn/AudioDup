-- Creates the database.
CREATE DATABASE `dejavu` IF NOT EXISTS;

-- Creates the song table.
CREATE TABLE `songs` (
  `song_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `song_name` varchar(250) NOT NULL,
  `fingerprinted` tinyint(4) DEFAULT '0',
  `file_sha1` binary(20) NOT NULL,
  PRIMARY KEY (`song_id`),
  UNIQUE KEY `song_id` (`song_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates the fingerprint table.
CREATE TABLE `fingerprints` (
  `hash` binary(10) NOT NULL,
  `song_id` mediumint(8) unsigned NOT NULL,
  `offset` int(10) unsigned NOT NULL,
  UNIQUE KEY `unique_constraint` (`song_id`,`offset`,`hash`),
  KEY `hash` (`hash`),
  CONSTRAINT `fingerprints_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates the md5 table.
CREATE TABLE `md5` (
  `video_name` varchar(30) NOT NULL DEFAULT '' COMMENT 'video file name without folder & extension',
  `md5_val` char(32) NOT NULL DEFAULT '' COMMENT 'the md5 value in hex string representation',
  PRIMARY KEY (`video_name`),
  INDEX `md5_val` (`md5_val`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates the video_hash table
CREATE TABLE `video_hash` (
  `id` INT AUTO_INCREMENT NOT NULL COMMENT 'auto increment ID',
  `video_name` VARCHAR(30) NOT NULL DEFAULT '' COMMENT 'video file name without folder & extension',
  `frame_id` SMALLINT NOT NULL DEFAULT 0 COMMENT 'frame ID inside the video',
  `hash_type` TINYINT NOT NULL DEFAULT 0 COMMENT 'the type of the hash value in this row',
  `hash_value` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT 'the hash value in json string format',
  PRIMARY KEY (`id`),
  INDEX `video_frame` (`video_name`, `frame_id`, `hash_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
