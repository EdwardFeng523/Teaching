//
//  ViewController.swift
//  FirstClassDemo
//
//  Created by Edward Feng on 2/11/18.
//  Copyright © 2018 Edward Feng. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var player_1: String = ""
    var player_2: String = ""
    @IBOutlet weak var label: UILabel!
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var helloWorld: UIButton!
    @IBAction func button(_ sender: UIButton) {
        if sender.currentTitle == "Start" {
            if player_1 == "rock" {
                if player_2 == "rock" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 0/255, blue: 255/255, alpha: 1)
                }
                if player_2 == "paper" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 255/255, blue: 0/255, alpha: 1)
                }
                if player_2 == "scissors" {
                    self.view.backgroundColor = UIColor(red: 255/255, green: 0/255, blue: 0/255, alpha: 1)
                }
            }
            if player_1 == "paper" {
                if player_2 == "rock" {
                    self.view.backgroundColor = UIColor(red: 255/255, green: 0/255, blue: 0/255, alpha: 1)
                }
                if player_2 == "paper" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 0/255, blue: 255/255, alpha: 1)
                }
                if player_2 == "scissors" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 255/255, blue: 0/255, alpha: 1)
                }
            }
            if player_1 == "scissors" {
                if player_2 == "rock" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 255/255, blue: 0/255, alpha: 1)
                }
                if player_2 == "paper" {
                    self.view.backgroundColor = UIColor(red: 255/255, green: 0/255, blue: 0/255, alpha: 1)
                }
                if player_2 == "scissors" {
                    self.view.backgroundColor = UIColor(red: 0/255, green: 0/255, blue: 255/255, alpha: 1)
                }
            }
            
        }
        if sender.currentTitle == "Player1" {
            player_1 = textField.text!
            
        }
        if sender.currentTitle == "Player2" {
            player_2 = textField.text!
        }
    }
    
}

