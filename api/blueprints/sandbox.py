from flask import Blueprint, render_template, jsonify, request, session

# Create the blueprint
sandbox_bp = Blueprint('sandbox', __name__)

# Sandbox Page Route (/sandbox)
@sandbox_bp.route('/sandbox')
def sandbox_page():
    high_score = session.get('sandbox_highscore', 0)
    return render_template('sandbox.html', high_score=high_score)

# High Score API Endpoint
@sandbox_bp.route('/api/save-score', methods=['POST'])
def save_score():
    data = request.get_json() or {}
    score = int(data.get('score', 0))
    
    current_high = session.get('sandbox_highscore', 0)
    if score > current_high:
        session['sandbox_highscore'] = score
        return jsonify({"status": "success", "new_record": True, "high_score": score})
        
    return jsonify({"status": "success", "new_record": False, "high_score": current_high})
