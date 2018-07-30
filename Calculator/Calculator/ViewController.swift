//
//  ViewController.swift
//  Calculator
//
//  Created by Edward Feng on 2/25/18.
//  Copyright © 2018 Edward Feng. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var isTyping = false
    @IBOutlet weak var display: UILabel!
    
    @IBAction func number(_ sender: UIButton) {
        if isTyping {
            display.text = display.text! + sender.currentTitle!
        } else {
            display.text = sender.currentTitle!
            isTyping = true
        }
        
    }
    

    @IBAction func del(_ sender: UIButton) {
        if display.text!.count == 1 {
            display.text = "0"
            isTyping = false
        } else {
            display.text = String(display.text!.dropLast())
        }
        
    }
    
    var displayValue: Double {
        get {
            return Double(display.text!)!
        }
        set {
            display.text = String(newValue)
        }
    }
    
    @IBAction func unaryOperation(_ sender: UIButton) {
        if let symbol = sender.currentTitle {
            isTyping = false
            switch symbol {
            case "π":
                displayValue = Double.pi
            case "√":
                displayValue = sqrt(displayValue)
            case "x²":
                displayValue = displayValue * displayValue
            case "1/x":
                displayValue = 1 / displayValue
            case "AC":
                display.text = "0"
            default:
                break
            }
        }
    }
    
    var previousNum: Double? = nil
    var sign: String? = nil
    
    @IBAction func binaryOperation(_ sender: UIButton) {
        if sign == nil {
            previousNum = displayValue
            sign = sender.currentTitle!
            isTyping = false
        } else {
            displayValue = performOperation()
            previousNum = displayValue
            sign = sender.currentTitle!
        }
        
    }
    
    @IBAction func equal(_ sender: UIButton) {
        displayValue = performOperation()
        previousNum = nil
        sign = nil
    }
    
    func performOperation() -> Double {
        if let symbol = sign {
            isTyping = false
            switch symbol {
            case "+":
                return previousNum! + displayValue
            case "-":
                return previousNum! - displayValue
            case "*":
                return previousNum! * displayValue
            default:
                return displayValue
            }
        }
        return displayValue
    }
    
}

