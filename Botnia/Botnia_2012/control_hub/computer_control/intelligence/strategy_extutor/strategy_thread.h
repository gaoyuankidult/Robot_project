//========================================================================
//  This software is free: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License Version 3,
//  as published by the Free Software Foundation.
//
//  This software is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  Version 3 in the file COPYING that came with this distribution.
//  If not, see <http://www.gnu.org/licenses/>.
//========================================================================
/*!
  \file    ClientThreading.h
  \brief   C++ Interface: ViewUpdateThread
  \author  Joydeep Biswas, Stefan Zickler (C) 2009
*/
//========================================================================

#ifndef STRATEGY_THREAD_H
#define STRATEGY_THREAD_H

#include <QThread>
#include <QVector>
#include <QPointF>
#include <QSemaphore>
#include "user_interface/field_related/field_robot.h"
#include "user_interface/field_related/field_ball.h"
#include "user_interface/strategy_control_window.h"
#include "net/net_vision_server.h"
#include "net/net_vision_client.h"
#include "net/net_radio_server.h"
#include "control_hub/computer_control/intelligence/strategy_extutor/strategy_thread.h"
#include "control_hub/computer_control/knowledge_base/database/world_state/field_world.h"
#include "control_hub/computer_control/intelligence/strategy_extutor/strategy.h"

#include "control_hub/human_control/joystick_gao.h"

// In many thread apllication people need to recursively include classes.
// This class should be declared here to indicate the name
class MainWindow;



enum RUNSTATUSTYPE{RUN_START,RUN_PAUSE,RUN_STEP,RUN_STOP};
enum STRATEGYTYPE{STRATEGY_RUN,STRATEGY_TEST,STRATEGY_JOYSTICK};
extern QMutex runstatusMutex;
extern double GetTimeSec();
// Strategy
extern Strategy strategy; // defined in the field_global_function.cpp
extern SSL_RadioFrame RadioCmds;
extern int iJoystickRobot;

struct RunStatus
{
    RUNSTATUSTYPE Status;		//运行，暂停 running status
    STRATEGYTYPE StrategyIndex;	//策略类型  strategy type
    double dFreq;					//策略运行频率 frequency
    char * tactic_name_;
};
extern QString sTactics[5];
extern RunStatus StatusOnGUI;	//策略状态

class StrategyThread : public QThread
{
    Q_OBJECT
private:
    //This parameter desides the whether it is joystick mode or normal mode
    // This is also the indicator of the whether "while 1" loop in the thread will continue or not
    bool thread_terminated_;
    // stores infomation whether it is thread mode or not
    bool bThreadMode;

    // Internal FieldView object for convinient modification
    FieldView *soccerView;
    // Storing the time interval of strategy
    double strategyGetTimeVal;
    // Storing the time interval for vision
    double visionGetTimeVal;
    //-------------------------------------
    unsigned long TickCount,oldTickCount;
    //-------------------------------------
     Joystick joystick;

public slots:

signals:
    void explains(); //如果要自定义槽和信号, explains信号是必须的
    void guiRefresh(void);//自定义信号.

public:
    StrategyThread();
    StrategyThread ( FieldView *_soccer ,bool _bThreadMode=true);

    // recieve from the vision
    void set_thread_terminated(bool thread_terminated){thread_terminated_ = thread_terminated;}
    bool do_vision_recv();
    bool do_refbox_recv();
    bool SkipVisionWait();
    void run();
    void terminate();
    void DoTactics();
    void do_StrategyJoystick();
    void ClearGuiTactic(int i);
    void ClearGuiTactics();
    inline bool IsStrategyOld();
};


#endif // STRATEGYTHREAD_H
