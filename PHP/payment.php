<?php
class Payment{
    public $id;

    public function __construct($id){
        $this->id=$id;
    }

    public function printDataPayment(){
        echo "ID Payment: ".$this->."<"
    }
}