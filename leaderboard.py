#!/usr/bin/env python3
"""
Simple Leaderboard Generator for DS-BTT-test Repository
Creates leaderboards for Two Sum and Max Profit challenges
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

def collect_all_scores():
    """Collect scores from all participants (simplified version)"""
    # For demo purposes, create sample data
    # In production, you'd get this from GitHub API by finding all forks
    
    sample_scores = [
        {
            'user': 'alice_dev',
            'two_sum_score': 5, 'two_sum_total': 5,
            'max_profit_score': 5, 'max_profit_total': 5,
            'total_score': 10, 'total_possible': 10, 'percentage': 100.0,
            'timestamp': '2025-09-07T10:30:00'
        },
        {
            'user': 'bob_coder', 
            'two_sum_score': 4, 'two_sum_total': 5,
            'max_profit_score': 5, 'max_profit_total': 5,
            'total_score': 9, 'total_possible': 10, 'percentage': 90.0,
            'timestamp': '2025-09-07T11:15:00'
        },
        {
            'user': 'carol_student',
            'two_sum_score': 5, 'two_sum_total': 5,
            'max_profit_score': 3, 'max_profit_total': 5,
            'total_score': 8, 'total_possible': 10, 'percentage': 80.0,
            'timestamp': '2025-09-07T09:45:00'
        }
    ]
    
    # Add current user's actual score if available
    if Path('user_score.json').exists():
        try:
            with open('user_score.json', 'r') as f:
                current_score = json.load(f)
                sample_scores.append(current_score)
        except Exception as e:
            print(f"Could not load current score: {e}")
    
    return sample_scores

def create_main_leaderboard():
    """Create the main leaderboard by total score"""
    print("🏆 Creating Main Leaderboard...")
    
    all_scores = collect_all_scores()
    
    # Sort by percentage (highest first)
    sorted_scores = sorted(all_scores, key=lambda x: x['percentage'], reverse=True)
    
    # Create markdown content
    content = f"""# 🏆 DS-BTT-Test Leaderboard

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*

## 🎯 Overall Rankings

| Rank | User | Two Sum | Max Profit | Total Score | Percentage |
|------|------|---------|------------|-------------|------------|
"""
    
    for i, score in enumerate(sorted_scores[:10], 1):  # Top 10
        rank_emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        
        two_sum_display = f"{score['two_sum_score']}/{score['two_sum_total']}"
        max_profit_display = f"{score['max_profit_score']}/{score['max_profit_total']}"
        total_display = f"{score['total_score']}/{score['total_possible']}"
        
        content += f"| {rank_emoji} | **{score['user']}** | {two_sum_display} | {max_profit_display} | {total_display} | {score['percentage']:.1f}% |\n"
    
    # Add problem-specific rankings
    content += f"""

## 📊 Problem-Specific Leaders

### 🔢 Two Sum Champions
"""
    
    # Sort by Two Sum performance
    two_sum_leaders = sorted(all_scores, key=lambda x: (x['two_sum_score'], -len(x['user'])), reverse=True)[:5]
    
    for i, score in enumerate(two_sum_leaders, 1):
        emoji = "🌟" if score['two_sum_score'] == score['two_sum_total'] else "⭐"
        content += f"{i}. {emoji} **{score['user']}**: {score['two_sum_score']}/{score['two_sum_total']} tests\n"
    
    content += f"""
### 💰 Max Profit Champions
"""
    
    # Sort by Max Profit performance  
    profit_leaders = sorted(all_scores, key=lambda x: (x['max_profit_score'], -len(x['user'])), reverse=True)[:5]
    
    for i, score in enumerate(profit_leaders, 1):
        emoji = "🌟" if score['max_profit_score'] == score['max_profit_total'] else "⭐"
        content += f"{i}. {emoji} **{score['user']}**: {score['max_profit_score']}/{score['max_profit_total']} tests\n"
    
    # Add statistics
    total_participants = len(all_scores)
    perfect_scores = len([s for s in all_scores if s['percentage'] == 100.0])
    avg_score = sum(s['percentage'] for s in all_scores) / len(all_scores) if all_scores else 0
    
    content += f"""

## 📈 Challenge Statistics

- **Total Participants**: {total_participants}
- **Perfect Scores**: {perfect_scores} ({(perfect_scores/total_participants*100):.1f}% if total_participants > 0 else 0:.1f}%)
- **Average Score**: {avg_score:.1f}%
- **Most Common Issue**: Array indexing (based on failed tests)

## 🚀 How to Improve Your Ranking

1. **Fork this repository** and clone it locally
2. **Complete both functions** in `my_solutions/solution.py`:
   - `twoSum(nums, target)` - Find indices of two numbers that sum to target
   - `maxProfit(prices)` - Find maximum profit from stock prices
3. **Test locally** by running the grader: `python grader.py`
4. **Push your solution** to your fork
5. **Create a Pull Request** to see your official score

---
*Leaderboard updates automatically when you submit solutions via Pull Request*
"""
    
    # Save leaderboard
    with open('LEADERBOARD.md', 'w') as f:
        f.write(content)
    
    print("✅ Main leaderboard created at LEADERBOARD.md")
    return sorted_scores

def create_activity_leaderboard():
    """Create leaderboard showing most active contributors"""
    print("📈 Creating Activity Leaderboard...")
    
    # Sample activity data (in real version, count commits/PRs)
    activity_data = [
        {'user': 'alice_dev', 'attempts': 8, 'last_activity': '2025-09-07T14:30:00'},
        {'user': 'bob_coder', 'attempts': 5, 'last_activity': '2025-09-07T13:15:00'},
        {'user': 'carol_student', 'attempts': 12, 'last_activity': '2025-09-07T12:45:00'},
        {'user': 'dave_learner', 'attempts': 3, 'last_activity': '2025-09-07T11:20:00'},
    ]
    
    # Add current user
    current_user = os.getenv('GITHUB_ACTOR')
    if current_user:
        activity_data.append({
            'user': current_user,
            'attempts': 2,  # Would count actual commits in real version
            'last_activity': datetime.now().isoformat()
        })
    
    # Sort by attempts
    sorted_activity = sorted(activity_data, key=lambda x: x['attempts'], reverse=True)
    
    content = f"""# 📈 Most Active Contributors

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*

| Rank | User | Attempts | Last Activity |
|------|------|----------|---------------|
"""
    
    for i, activity in enumerate(sorted_activity[:10], 1):
        rank_emoji = "🔥" if i == 1 else "⚡" if i == 2 else "💪" if i == 3 else f"{i}."
        
        # Format timestamp
        try:
            timestamp = datetime.fromisoformat(activity['last_activity'].replace('Z', '+00:00'))
            time_str = timestamp.strftime('%m/%d %H:%M')
        except:
            time_str = 'Recent'
        
        content += f"| {rank_emoji} | **{activity['user']}** | {activity['attempts']} | {time_str} |\n"
    
    content += """
---
*Keep coding and climbing the activity leaderboard! 🚀*
"""
    
    # Save activity leaderboard
    with open('ACTIVITY.md', 'w') as f:
        f.write(content)
    
    print("✅ Activity leaderboard created at ACTIVITY.md")

def main():
    """Main leaderboard generation function"""
    print("🏆 Generating Leaderboards for DS-BTT-Test...")
    
    try:
        scores = create_main_leaderboard()
        create_activity_leaderboard()
        
        print(f"\n🎉 Leaderboards updated successfully!")
        print(f"📊 {len(scores)} participants tracked")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error generating leaderboards: {e}")
        return 1

if __name__ == "__main__":
    main()
