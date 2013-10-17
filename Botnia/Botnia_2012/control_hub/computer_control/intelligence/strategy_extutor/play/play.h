// play.h
//
// Encapsulates team behavior.
//
// Created by:  Michael Bowling (mhb@cs.cmu.edu)
//
/* LICENSE:
  =========================================================================
    CMDragons'02 RoboCup F180 Source Code Release
  -------------------------------------------------------------------------
    Copyright (C) 2002 Manuela Veloso, Brett Browning, Mike Bowling,
                       James Bruce; {mmv, brettb, mhb, jbruce}@cs.cmu.edu
    School of Computer Science, Carnegie Mellon University
  -------------------------------------------------------------------------
    This software is distributed under the GNU General Public License,
    version 2.  If you do not have a copy of this licence, visit
    www.gnu.org, or write: Free Software Foundation, 59 Temple Place,
    Suite 330 Boston, MA 02111-1307 USA.  This program is distributed
    in the hope that it will be useful, but WITHOUT ANY WARRANTY,
    including MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  ------------------------------------------------------------------------- */

#ifndef __play_h__
#define __play_h__

#include <vector>
#include "control_hub/computer_control/knowledge_base/database/world_state/field_world.h"
#include "control_hub/computer_control/intelligence/strategy_extutor/tactic/base_tactic.h"




#define MAX_PLAY_ROLES 4

//жϷֵҪϢ

//
// PlayRole
//

class PlayRole
{
public:
	vector<Tactic *> tactics;

	// Constructors
	PlayRole(Tactic *t, ...);
	//ӲԿȡɫϢ;
	PlayRole(const char *string, int &n, bool &error);

	Tactic *operator [](uint index) const
	{
		if (index < tactics.size())
		{
			return tactics[index];
		}
		else return NULL;
	}
};

//
// Play
//
//жϷֵҪϢΪһ
class Play
{
protected:
	vector<PlayRole> roles;

public:
	char *name;

	virtual ~Play() { }

	uint length();
	PlayRole &getRole(int priority)
	{
		return roles[priority];
	}

	virtual int &getFixedRoleID(int robot)
	{
		static int irobot=robot;
		return irobot;
	}

	virtual bool isApplicable(World &w)
	{
		return true;
	}
	virtual Status isDone(World &w)
	{
		return InProgress;
	}
	virtual double timeout()
	{
		return -1;
	}

	virtual void updateOpponentMap(World &w, TRoleMap *m) { }
};

//
// WorldPredicate
//

typedef bool (*WorldPredicate)(World &world, double argument);

class WorldPredicateConjunct
{
private:
	//
	vector<WorldPredicate> predicate;

	vector<bool> predicate_negated;
	//
	vector<double> predicate_argument;

public:
	bool eval(World &world)
	{
		for (uint i=0; i<predicate.size(); i++)
		{
			if (! (predicate_negated[i] ^ (predicate[i])(world, predicate_argument[i])) )
			{
				return false;
			}
		}
		return true;
	}

	void add(WorldPredicate p, bool negated, double argument)
	{
		predicate.push_back(p);
		predicate_negated.push_back(negated);
		predicate_argument.push_back(argument);
	}

	void clear()
	{
		predicate.clear();
		predicate_negated.clear();
		predicate_argument.clear();
	}
};

//
// OpponentRole
//

typedef int (*OpponentRole)(World &world, bool candidates[]);

//
// PlayAscii
//

class PlayAscii : public Play
{
private:
	vector<WorldPredicateConjunct> applicable;

	vector<WorldPredicateConjunct> done;
	vector<Status> done_status;

	vector<int> fixed_roles;

	//õĶֽɫֲ
	//Ҫ˽ĶԷ˽ɫ
	vector<OpponentRole> opponent_roles;

	double play_timeout;

	bool parse(const char *string, int &n);
	void printErrorLine(const char *string, int n);

	//
	// Predicates	ν
	//

	//
	static bool pred_offense(World &w, double a)
	{
		return w.situation == World::Offense;
	}
	//
	static bool pred_defense(World &w, double a)
	{
		return w.situation == World::Defense;
	}
	//ֿ
	static bool pred_their_ball(World &w, double a)
	{
		return w.possession == World::TheirBall;
	}
	//
	static bool pred_our_ball(World &w, double a)
	{
		return w.possession == World::OurBall;
	}
	//˫
	static bool pred_loose_ball(World &w, double a)
	{
		return w.possession == World::LooseBall;
	}

	//ڶԷ볡
	static bool pred_their_side(World &w, double a)
	{
		return w.fieldPosition == World::TheirSide;
	}
	//ڼ볡
	static bool pred_our_side(World &w, double a)
	{
		return w.fieldPosition == World::OurSide;
	}
	//г
	static bool pred_midfield(World &w, double a)
	{
		return w.fieldPosition == World::Midfield;
	}

	//ڼ
	static bool pred_in_our_corner(World &w, double a)
	{
		return (w.ballXThreshold < (-FIELD_LENGTH_H +
		                            DEFENSE_DEPTH + ROBOT_DEF_WIDTH_H) &&
		        fabs(w.ballYThreshold) > DEFENSE_WIDTH_H);
	}
	//ڶԷ
	static bool pred_in_their_corner(World &w, double a)
	{
		return (w.ballXThreshold > (FIELD_LENGTH_H -
		                            DEFENSE_DEPTH - ROBOT_DEF_WIDTH_H) &&
		        fabs(w.ballYThreshold) > DEFENSE_WIDTH_H);
	}

	//
	static bool pred_our_kickoff(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == 'K') ||
		       (w.color_ == TEAM_YELLOW && w.game_state == 'k');
	}
	//Է
	static bool pred_their_kickoff(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == 'k') ||
		       (w.color_ == TEAM_YELLOW && w.game_state == 'K');
	}
	//ֱ
	static bool pred_our_freekick(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == 'F') ||
		       (w.color_ == TEAM_YELLOW && w.game_state == 'f');
	}
	//Էֱ
	static bool pred_their_freekick(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == 'f') ||
		       (w.color_ == TEAM_YELLOW && w.game_state == 'F');
	}

	//Է
	static bool pred_their_penalty(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == COMM_PENALTY_YELLOW) ||
		       (w.color_ == TEAM_YELLOW && w.game_state == COMM_PENALTY_BLUE);
	}
	//
	static bool pred_our_penalty(World &w, double a)
	{
		return (w.color_ == TEAM_BLUE && w.game_state == COMM_PENALTY_BLUE) ||
		       (w.color_ == TEAM_YELLOW && w.game_state == COMM_PENALTY_YELLOW);
	}
	//Xָ
	static bool pred_ball_x_gt(World &w, double a)
	{
		return (a < w.ballXThreshold);
	}
	//XСָ
	static bool pred_ball_x_lt(World &w, double a)
	{
		return (a > w.ballXThreshold);
	}

	//Yֵֵָ
	static bool pred_ball_absy_gt(World &w, double a)
	{
		return (a < fabs(w.ballYThreshold));
	}
	//YֵСֵָ
	static bool pred_ball_absy_lt(World &w, double a)
	{
		return (a > fabs(w.ballYThreshold));
	}

	//жϼԷڼ볡
	static bool pred_nopponents_our_side(World &w, double a)
	{
		int n = 0;
		for (int i=0; i<w.n_opponents; i++)
		{
			if (w.opponent_position(i).x < -400)
			{
				n++;
			}
		}
		return (n >= a);
	}

	//
	// Opponent Roles
	//

	//ȷŶԱ;
	static int orole_best_shot(World &world, bool candidates[]);
	//ȷڶԷ볡ǰ(ӽг)Ա;
	static int orole_most_downfield(World &world, bool candidates[]);
	//ȷҷ볡ǰԱ;
	static int orole_most_upfield(World &world, bool candidates[]);

	static int orole_goalie(World &world, bool candidates[]);
	//ȷԷĶԱ;
	static int orole_closest_to_ball(World &world, bool candidates[]);
	//ȷԷλĶԱ;
	static int orole_closest_to_shot(World &world, bool candidates[]);
	static int orole_best_pass(World &world, bool candidates[]);

	//
	// Parsing Methods
	//

	WorldPredicateConjunct &parsePredicate(const char *string, int &n);
	OpponentRole parseORole(const char *string, int &n);

public:
	PlayAscii(const char *string, int &n, bool &error);
	PlayAscii(const char *filename, bool &error);

	//ù̶ɫ
	virtual int getRoleFixedID(int fixed)
	{
		return fixed_roles[fixed];
	}

	//playǷһͿ
	virtual bool isApplicable(World &w)
	{
		for (uint i=0; i<applicable.size(); i++)
		{
			if (applicable[i].eval(w))
			{
				return true;
			}
		}
		return false;
	}

	//playжϣֻҪһ㣬
	virtual Status isDone(World &w)
	{
		for (uint i=0; i<done.size(); i++)
		{
			if (done[i].eval(w))
			{
				return done_status[i];
			}
		}
		return InProgress;
	}

	//ȡʱʱ
	virtual double timeout()
	{
		return play_timeout;
	}

	//¶Էͼ
	virtual void updateOpponentMap(World &w, TRoleMap *m)
	{
		bool candidates[MAX_TEAM_ROBOTS];
		for (int i=0; i<MAX_TEAM_ROBOTS; i++)
		{
			candidates[i] = true;
		}
		m->clear();
		//ֽɫ
		for (uint i=0; i<opponent_roles.size(); i++)
		{
			//ݽűҪ֪ĶֽɫҪȷ־ָ߱ɫĻ
			//磬closest_to_ball »
			//closest_to_shot  
			int id = (opponent_roles[i])(w, candidates);
			if (id >= 0)
			{
				m->push_back(id);
				candidates[id] = false;
			}
		}
	}

};

#endif
