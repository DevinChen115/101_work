<?php

function getConnection(){
    try{
        $conn = new PDO("mysql:host=localhost;dbname=NoteForSection;charset=utf8mb4","root","admin");
        return $conn;
    }catch(PDOException $e){
        $e->getMessage();
    }
}

function getTables($conn){
    $sql = "show tables";
    $result = $conn->query($sql);
    return $result->fetchAll(PDO::FETCH_COLUMN);
}

function getValueByProject($conn,$project){
    $sql = 'SELECT * FROM '.$project.' ORDER BY section';
    $result = $conn->query($sql);
    return $result->fetchAll();
}

function createProject($conn,$proName){
    $sql = 'CREATE TABLE `'.$proName.'` ( `section` VARCHAR(50) NOT NULL ,`version` VARCHAR(20) NOT NULL , `note` TEXT NOT NULL , PRIMARY KEY(`section`)) ENGINE = MyISAM';
    $conn->exec($sql);
    if($conn->errorCode() != 00000){
        return $conn->errorInfo();
    }
    return "新增 ".$proName." 成功";    
}

function deleteProject($conn,$proName){
    $sql = 'DROP TABLE `'.$proName.'`';
    $conn->exec($sql);
    if($conn->errorCode() != 00000){
        return $conn->errorInfo();
    }
    return "刪除 ".$proName." 成功";
}

function insertSection($conn,$project,$section,$ver,$note){
    $sql = 'INSERT INTO '.$project.'(version,section,note) VALUES("'.$ver.'","'.$section.'","'.$note.'");';
    $conn->exec($sql);
    if($conn->errorCode() != 00000){
        return $conn->errorInfo();
    }
    return "新增 ".$section." 成功";
}

function deleteSection($conn,$proName,$section){
    $sql="DELETE FROM `".$proName."` WHERE section='".$section."'";
    $conn->exec($sql);
    if($conn->errorCode() != 00000){
        return $conn->errorInfo();
    }
    return "刪除 ".$section." 成功";
}

function modifySection($conn,$proName,$section,$note){
    $sql = "UPDATE `".$proName."` SET note='".$note."' WHERE section='".$section."'";
    $conn->exec($sql);
    if($conn->errorCode() != 00000){
        return $conn->errorInfo();
    }
    return "修改 ".$section." 成功";
}
