-- phpMyAdmin SQL Dump
-- version 3.3.9.2
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2011 年 04 月 26 日 09:51
-- 服务器版本: 5.1.49
-- PHP 版本: 5.3.3-1ubuntu9.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `yapm`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `admin` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `priv` int(2) NOT NULL,
  `last_login_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_login_ipadd` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `admin`
--


-- --------------------------------------------------------

--
-- 表的结构 `fees`
--

CREATE TABLE IF NOT EXISTS `fees` (
  `name` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `sum` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `status` varchar(64) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `fees`
--


-- --------------------------------------------------------

--
-- 表的结构 `mail`
--

CREATE TABLE IF NOT EXISTS `mail` (
  `mail_no` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(1024) NOT NULL,
  `target` varchar(128) NOT NULL,
  `source` varchar(128) NOT NULL,
  `status` varchar(16) NOT NULL,
  `reply_for` int(11) NOT NULL,
  UNIQUE KEY `mail_no` (`mail_no`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `mail`
--


-- --------------------------------------------------------

--
-- 表的结构 `member_of_family`
--

CREATE TABLE IF NOT EXISTS `member_of_family` (
  `username` varchar(128) NOT NULL,
  `member_of_family` varchar(64) NOT NULL COMMENT '真实名称',
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `member_of_family`
--


-- --------------------------------------------------------

--
-- 表的结构 `message`
--

CREATE TABLE IF NOT EXISTS `message` (
  `message_no` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(1024) NOT NULL,
  `post_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `poster` varchar(128) NOT NULL,
  `reply_content` varchar(1024) NOT NULL,
  `reply_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `replyer` varchar(128) NOT NULL,
  UNIQUE KEY `message_no` (`message_no`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `message`
--


-- --------------------------------------------------------

--
-- 表的结构 `news`
--

CREATE TABLE IF NOT EXISTS `news` (
  `news_no` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `content` varchar(1024) NOT NULL,
  `validity_time` date NOT NULL,
  `poster` varchar(128) NOT NULL,
  `last_modify` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `news_no` (`news_no`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `news`
--


-- --------------------------------------------------------

--
-- 表的结构 `trouble`
--

CREATE TABLE IF NOT EXISTS `trouble` (
  `trouble_no` int(11) NOT NULL,
  `desc` varchar(2046) NOT NULL,
  `reporter` varchar(128) NOT NULL,
  `status` varchar(32) NOT NULL,
  `post_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `priv` int(2) NOT NULL,
  `worker_no` varchar(32) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `trouble`
--


-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `user`
--


-- --------------------------------------------------------

--
-- 表的结构 `user_detail`
--

CREATE TABLE IF NOT EXISTS `user_detail` (
  `username` varchar(128) NOT NULL,
  `building_no` varchar(128) NOT NULL,
  `unit_no` varchar(128) NOT NULL,
  `house_number` varchar(128) NOT NULL,
  `tel` int(32) DEFAULT NULL,
  `mobile` int(16) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `user_detail`
--


-- --------------------------------------------------------

--
-- 表的结构 `worker`
--

CREATE TABLE IF NOT EXISTS `worker` (
  `worker_no` varchar(32) NOT NULL,
  `password` varchar(128) NOT NULL,
  `status` varchar(64) NOT NULL,
  `location` varchar(256) NOT NULL,
  `load` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `worker`
--

