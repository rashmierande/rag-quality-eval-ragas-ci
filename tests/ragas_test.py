import json
import os
import sys
from datasets import Dataset
from llm_config import get_ragas_llm, get_ragas_embeddings
from ragas import evaluate, RunConfig
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

def load_test_data():
    """Load test data from JSON file"""
    with open('tests/test_data.json', 'r') as f:
        return json.load(f)

def run_ragas_evaluation():
    """Run RAGAS evaluation on test dataset"""
    
    print("=" * 60)
    print("RAGAS Quality Evaluation")
    print("=" * 60)
    
    # Load test data
    print("\n📂 Loading test data...")
    test_data = load_test_data()
    print(f"✓ Loaded {len(test_data)} test cases")
    
    # Convert to RAGAS dataset format
    dataset = Dataset.from_dict({
        'question': [item['question'] for item in test_data],
        'answer': [item['answer'] for item in test_data],
        'contexts': [item['contexts'] for item in test_data],
        'ground_truth': [item['ground_truth'] for item in test_data]
    })
    dataset = dataset.select(range(2))

    
    # Run evaluation
    print("\n🤖 Running RAGAS evaluation...")
    result = evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall
        ],
        llm=get_ragas_llm(),
        embeddings=get_ragas_embeddings(),
        run_config=RunConfig(max_workers=1),
    )
    
    # Convert to dict
    #results = result.to_pandas().mean().to_dict()
    df = result.to_pandas()
    numeric_cols = df.select_dtypes(include=["number"]).columns
    results = df[numeric_cols].mean().to_dict()
    
    # Add pass/fail status
    thresholds = {
        'faithfulness': 0.7,
        'answer_relevancy': 0.7,
        'context_precision': 0.7,
        'context_recall': 0.7
    }
    
    all_passed = all(results.get(metric, 0) >= threshold 
                     for metric, threshold in thresholds.items())
    
    results['all_passed'] = all_passed
    
    # Save results
    with open('test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    for metric, threshold in thresholds.items():
        score = results.get(metric, 0)
        status = "✅ PASS" if score >= threshold else "❌ FAIL"
        print(f"{metric:20s}: {score:.4f} (threshold: {threshold}) {status}")
    
    print("=" * 60)
    
    # Check thresholds
    failed = []
    for metric, threshold in thresholds.items():
        if results.get(metric, 0) < threshold:
            failed.append(f"{metric} ({results[metric]:.4f} < {threshold})")
    
    if failed:
        print("\n❌ TESTS FAILED:")
        for failure in failed:
            print(f"  - {failure}")
        print("\n💡 Tip: Review your prompts and ensure answers are grounded in context")
        sys.exit(1)
    else:
        print("\n✅ ALL TESTS PASSED!")
        print("Safe to merge! 🚀")
        sys.exit(0)

if __name__ == "__main__":
    run_ragas_evaluation()
